# 考研数学历年真题图片库

2009-2025 年考研数学一、数学二、数学三全部真题图片及答案，数据来源于 [真题墙](https://zhentiqiang.com/kaoyan/math)。

## 数据概览

| 项目 | 数量 |
|------|------|
| 试卷组 | 3（数学一 / 数学二 / 数学三） |
| 年份范围 | 2009 - 2025（共 17 年） |
| 题目总数 | 1,158 道 |
| 图片总数 | 3,032 张 |
| 总大小 | ~532 MB |

## 目录结构

```
kaoyan_math_images/
├── 数学一/
│   ├── answers.json              # 全部题目的答案与元数据
│   ├── 2025/
│   │   ├── Q01_id665.png         # 题目图片
│   │   ├── Q02_id663.png
│   │   ├── ...
│   │   ├── answers/              # 答案图片（仅非选择题）
│   │   │   ├── Q09_id645_answer.png
│   │   │   └── ...
│   │   └── analysis/             # 解析图片
│   │       ├── Q01_id665_analysis.png
│   │       └── ...
│   ├── 2024/
│   ├── ...
│   └── 2009/
├── 数学二/
│   └── ...
└── 数学三/
    └── ...
```

## 文件命名规则

### 题目图片

```
Q{题号两位数}_id{题目ID}.png
```

例如 `Q01_id665.png` 表示 2025 年数学一第 1 题，系统 ID 为 665。

### 答案图片

```
Q{题号两位数}_id{题目ID}_answer.png
```

**注意：** 选择题（第 1-8 题，`type=1`）没有答案图片，答案为单个字母，记录在 `answers.json` 中。

### 解析图片

```
Q{题号两位数}_id{题目ID}_analysis.png
```

每道题都有对应的解析图片，通常为 500KB-1MB 的详细解答过程。

## answers.json 说明

每个试卷组目录下有一个 `answers.json`，包含所有题目的元数据：

```json
{
  "数学一_2025_Q01": {
    "group": "数学一",
    "paper": "2025",
    "index": 1,
    "question_id": 665,
    "type": 1,
    "answer": "B",
    "score": 5,
    "knowledge_point": "曲线的凹凸性、拐点及渐近线",
    "video_url": "https://www.bilibili.com/video/BV1Ut411p7k3?p=87&t=10"
  }
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `group` | 试卷组（数学一 / 数学二 / 数学三） |
| `paper` | 年份（如 "2025"） |
| `index` | 题号（1-23） |
| `question_id` | 系统中的唯一题目 ID |
| `type` | 题目类型：`1` = 选择题，`2` = 填空/解答题 |
| `answer` | 选择题答案（如 "B"），非选择题为 `null` |
| `score` | 分值 |
| `knowledge_point` | 考点名称 |
| `video_url` | B 站名师讲解视频链接 |

## 题目类型对应关系

| 题号 | 类型 | 答案形式 |
|------|------|----------|
| Q01 - Q08 | 选择题（type=1） | `answers.json` 中的字母（如 "B"） |
| Q09 - Q10 | 填空题（type=2） | 答案图片 + 解析图片 |
| Q11 - Q23 | 解答题（type=2） | 答案图片 + 解析图片 |

## 重复题说明

数学一、数学二、数学三在同一年份中存在部分重复题目（共用同一道题），这些题的 `question_id` 相同，图片内容一致。

## 下载脚本

`download_math_images.py` 用于从 [真题墙](https://zhentiqiang.com/kaoyan/math) API 批量下载图片和答案数据。已下载的文件会自动跳过，支持断点续传。

```bash
python3 download_math_images.py
```

## 数据来源

- 题目与解析图片来源：[真题墙](https://zhentiqiang.com/kaoyan/math)
- 解析内容节选自《李艳芳真题及解析》
