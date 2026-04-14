#!/usr/bin/env python3
"""Download all 考研数学真题 images + answers from zhentiqiang.com"""

import json
import os
import time
import urllib.request
import urllib.error

BASE_URL = "https://zhentiqiang.com"
OUTPUT_DIR = "/Users/lixin/claude-docker/kaoyan_math_images"

GROUPS = {
    8: "数学一",
    9: "数学二",
    10: "数学三",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_json(url: str, retries: int = 3) -> dict | list | None:
    """Fetch JSON from URL with retry logic."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            print(f"  [retry {attempt+1}/{retries}] {url}: {e}")
            time.sleep(2 * (attempt + 1))
    return None


def download_file(url: str, filepath: str) -> bool:
    """Download a file, skip if already exists."""
    if os.path.exists(filepath):
        return True
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            if len(data) < 100:
                return False
            with open(filepath, "wb") as f:
                f.write(data)
            return True
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        if hasattr(e, "code") and e.code == 404:
            return False
        print(f"  [ERROR] {url}: {e}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_downloaded = 0
    total_skipped = 0
    total_failed = 0
    answers_collected: dict[str, dict] = {}

    for group_id, group_name in GROUPS.items():
        print(f"\n{'='*60}")
        print(f"Fetching papers for {group_name} (group_id={group_id})...")
        print(f"{'='*60}")

        papers_data = fetch_json(f"{BASE_URL}/api/papers/{group_id}")
        if not papers_data:
            print(f"  Failed to fetch papers for {group_name}, skipping.")
            continue

        if isinstance(papers_data, dict) and "papers" in papers_data:
            papers = papers_data["papers"]
        elif isinstance(papers_data, list):
            papers = papers_data
        else:
            print(f"  Unexpected data format: {type(papers_data)}")
            continue

        print(f"  Found {len(papers)} papers")

        for paper in papers:
            paper_id = paper["id"]
            paper_name = paper.get("name", str(paper_id))
            questions = paper.get("questions", [])

            if not questions:
                print(f"  Paper {paper_name} (id={paper_id}): no questions, skipping.")
                continue

            print(f"\n  Paper {paper_name} (id={paper_id}): {len(questions)} questions")

            for q in questions:
                q_id = q["id"]
                q_index = q.get("index", q_id)
                q_type = q.get("question_type", 1)

                q_dir = os.path.join(OUTPUT_DIR, group_name, paper_name)
                os.makedirs(q_dir, exist_ok=True)

                # === 1. Question image ===
                q_img_url = f"{BASE_URL}/static/photos/group_{group_id}/paper_{paper_id}/{q_index}.png"
                q_img_path = os.path.join(q_dir, f"Q{q_index:02d}_id{q_id}.png")

                if download_file(q_img_url, q_img_path):
                    total_downloaded += 1
                    status = "OK"
                elif os.path.exists(q_img_path):
                    total_skipped += 1
                    status = "CACHED"
                else:
                    total_failed += 1
                    status = "MISSING"

                # === 2. Answer image (non-choice questions) ===
                a_dir = os.path.join(q_dir, "answers")
                os.makedirs(a_dir, exist_ok=True)
                a_img_url = f"{BASE_URL}/static/photos/answer_images/{q_id}.png"
                a_img_path = os.path.join(a_dir, f"Q{q_index:02d}_id{q_id}_answer.png")
                download_file(a_img_url, a_img_path)

                # === 3. Analysis image ===
                an_dir = os.path.join(q_dir, "analysis")
                os.makedirs(an_dir, exist_ok=True)
                an_img_url = f"{BASE_URL}/static/photos/analysis_images/{q_id}.png"
                an_img_path = os.path.join(an_dir, f"Q{q_index:02d}_id{q_id}_analysis.png")
                download_file(an_img_url, an_img_path)

                # === 4. Fetch answer text via API (for choice questions) ===
                answer_key = f"{group_name}_{paper_name}_Q{q_index:02d}"
                if answer_key not in answers_collected:
                    q_info = fetch_json(f"{BASE_URL}/api/question_info/{q_id}")
                    if q_info and isinstance(q_info, dict) and q_info.get("success"):
                        answers_collected[answer_key] = {
                            "group": group_name,
                            "paper": paper_name,
                            "index": q_index,
                            "question_id": q_id,
                            "type": q_type,
                            "answer": q_info.get("answer", ""),
                            "score": q_info.get("score", ""),
                            "knowledge_point": q_info.get("knowledge_point_name", ""),
                            "video_url": q_info.get("video_url", ""),
                        }

                print(f"    Q{q_index:02d} (id={q_id}): question [{status}]")
                time.sleep(0.05)

            # Save answers for this group incrementally
            answers_file = os.path.join(OUTPUT_DIR, group_name, "answers.json")
            existing: dict = {}
            if os.path.exists(answers_file):
                with open(answers_file, encoding="utf-8") as f:
                    existing = json.load(f)
            group_answers = {k: v for k, v in answers_collected.items() if v["group"] == group_name}
            existing.update(group_answers)
            with open(answers_file, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            print(f"  Saved answers to {answers_file}")

    # Final summary
    print(f"\n{'='*60}")
    print(f"Download complete!")
    print(f"  Downloaded: {total_downloaded}")
    print(f"  Cached (already existed): {total_skipped}")
    print(f"  Failed/missing: {total_failed}")
    print(f"  Answers collected: {len(answers_collected)}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
