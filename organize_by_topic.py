#!/usr/bin/env python3
"""Organize math exam images by knowledge point (考点分类)."""

import json
import os
import shutil
import urllib.request
import urllib.error

BASE_URL = "https://zhentiqiang.com"
SOURCE_DIR = "/Users/lixin/claude-docker/kaoyan_math_images"
OUTPUT_DIR = "/Users/lixin/claude-docker/kaoyan_math_by_topic"

GROUPS = {
    8: "数学一",
    9: "数学二",
    10: "数学三",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_json(url: str) -> dict | list | None:
    """Fetch JSON from URL."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  [ERROR] {url}: {e}")
        return None


def build_tag_map(tree: list) -> dict[int, str]:
    """Build flat {id: "大类/章节/考点"} map from knowledge tree."""
    tag_map: dict[int, str] = {}

    def walk(nodes: list, prefix: str = "") -> None:
        for node in nodes:
            name = node["name"]
            path = f"{prefix}/{name}" if prefix else name
            if not node["children"]:
                tag_map[node["id"]] = path
            else:
                walk(node["children"], path)

    walk(tree)
    return tag_map


def copy_or_link(src: str, dst: str) -> bool:
    """Copy file, skip if exists."""
    if os.path.exists(dst):
        return True
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    return True


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total_linked = 0

    for group_id, group_name in GROUPS.items():
        print(f"\n{'='*60}")
        print(f"Processing {group_name} (group_id={group_id})...")
        print(f"{'='*60}")

        # 1. Fetch knowledge tree
        tree = fetch_json(f"{BASE_URL}/api/knowledge_tree/{group_id}")
        if not tree:
            continue
        tag_map = build_tag_map(tree)
        print(f"  Knowledge points: {len(tag_map)}")

        # 2. Fetch all papers with questions
        papers_data = fetch_json(f"{BASE_URL}/api/papers/{group_id}")
        if not papers_data:
            continue
        if isinstance(papers_data, dict) and "papers" in papers_data:
            papers = papers_data["papers"]
        elif isinstance(papers_data, list):
            papers = papers_data
        else:
            continue

        # 3. Build question lookup from source
        # Index: question_id -> source file paths
        q_source: dict[int, dict] = {}
        group_dir = os.path.join(SOURCE_DIR, group_name)
        for paper in papers:
            paper_name = paper.get("name", str(paper["id"]))
            paper_dir = os.path.join(group_dir, paper_name)
            for q in paper.get("questions", []):
                q_id = q["id"]
                q_index = q.get("index", q_id)
                entry: dict = {
                    "year": paper_name,
                    "index": q_index,
                    "question_img": os.path.join(paper_dir, f"Q{q_index:02d}_id{q_id}.png"),
                    "answer_img": os.path.join(paper_dir, "answers", f"Q{q_index:02d}_id{q_id}_answer.png"),
                    "analysis_img": os.path.join(paper_dir, "analysis", f"Q{q_index:02d}_id{q_id}_analysis.png"),
                }
                q_source[q_id] = entry

        # 4. Organize by knowledge point
        topic_index: dict[str, list] = {}
        for paper in papers:
            for q in paper.get("questions", []):
                q_id = q["id"]
                tag_id = q.get("knowledge_tags_id")
                if not tag_id or tag_id not in tag_map:
                    continue

                topic_path = tag_map[tag_id]
                src = q_source.get(q_id)
                if not src:
                    continue

                # Target: kaoyan_math_by_topic/数学一/高等数学/函数、极限、连续/函数极限的计算/2025_Q01.png
                topic_dir = os.path.join(OUTPUT_DIR, group_name, topic_path)

                # Copy question image
                q_dst = os.path.join(topic_dir, f"{src['year']}_Q{src['index']:02d}.png")
                if os.path.exists(src["question_img"]):
                    copy_or_link(src["question_img"], q_dst)

                # Copy analysis image
                a_dst = os.path.join(topic_dir, "analysis", f"{src['year']}_Q{src['index']:02d}_analysis.png")
                if os.path.exists(src["analysis_img"]):
                    copy_or_link(src["analysis_img"], a_dst)

                # Copy answer image
                ans_dst = os.path.join(topic_dir, "answers", f"{src['year']}_Q{src['index']:02d}_answer.png")
                if os.path.exists(src["answer_img"]):
                    copy_or_link(src["answer_img"], ans_dst)

                # Track for index
                if topic_path not in topic_index:
                    topic_index[topic_path] = []
                topic_index[topic_path].append({
                    "year": src["year"],
                    "index": src["index"],
                    "question_id": q_id,
                })
                total_linked += 1

        # 5. Save topic index
        index_path = os.path.join(OUTPUT_DIR, group_name, "topic_index.json")
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(topic_index, f, ensure_ascii=False, indent=2)
        print(f"  Organized {total_linked} questions into {len(topic_index)} topics")
        print(f"  Saved index to {index_path}")

    print(f"\n{'='*60}")
    print(f"Done! Total questions organized: {total_linked}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
