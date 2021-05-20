# docker-python-cronjob
foxit interview test

# Foxit Software Data Engineer Interview Question

1. Write a SQL query command for a report that provides the following information for each document in the `Document` table, regardless if there is an content for each of those documents.

SELECT D.Author, D.Title, C.Metadata AS Subtype, C.Content FROM Document D INNER JOIN
Content C ON D.DocumentId = C.DocumentId

```
Author, Title, Subtype, Content
```

**__Schema__**

```
Table: Document

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| DocumentId  | int     | PK
| Author      | varchar |
| Title       | varchar |
+-------------+---------+

Table: Content

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| ContentId   | int     | PK
| DocumentId  | int     |
| Metadata    | varchar |
| Content     | varchar |
+-------------+---------+
```

2. Use any tool that you are comfortable with to process this JSON file into required output schema. The output should be JSON lines for each block of `result` in `completions`. The `label` would be `htmllabels`, `sentence` would be `text` of each result and `contract_id` would be `data.filename` and remove the suffix `.html`. 
(Optional) Please sort these json lines by ascending order of interval between `endOffset` and `startOffset`.

* Required output schema 
```json
{
    "label": "Contract Title",
    "sentence": "Mutual Confidentiality and Non-Disclosure Agreement",
    "contract_id": "1qpqQsbhhUq"
}
```
* `raw.json`
```json
{
    "completions": [
        {
            "created_at": 1612850273,
            "id": 2001,
            "lead_time": 2552.251,
            "result": [
                {
                    "from_name": "ner",
                    "id": "IpAlj7cp63",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/h1[1]/a[1]/text()[1]",
                        "endOffset": 24,
                        "htmllabels": [
                            "Contract Title"
                        ],
                        "start": "/h1[1]/text()[1]",
                        "startOffset": 0,
                        "text": "Mutual Confidentiality and Non-Disclosure Agreement"
                    }
                },
                {
                    "from_name": "ner",
                    "id": "GrK2W6QwCs",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/p[2]/text()[1]",
                        "endOffset": 352,
                        "htmllabels": [
                            "Commencement"
                        ],
                        "start": "/p[2]/text()[1]",
                        "startOffset": 0,
                        "text": "In order to protect certain confidential information which may be disclosed between them, NewNet Communication Technologies, LLC and the undersigned company (each referred to as a “Party” or collectively as the “Parties”) agree to the following terms and conditions (the “Agreement”) to cover disclosure of the Confidential Information described below:"
                    }
                },
                {
                    "from_name": "ner",
                    "id": "gXVcsH6WEX",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/p[21]/text()[2]",
                        "endOffset": 155,
                        "htmllabels": [
                            "CI Definition"
                        ],
                        "start": "/p[21]/text()[2]",
                        "startOffset": 2,
                        "text": "Either Party may terminate this Agreement by giving the other Party written notice thereof at least thirty (30) days prior to the effective date thereof."
                    }
                },
                {
                    "from_name": "ner",
                    "id": "mNB7O1NnNG",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/p[21]/text()[3]",
                        "endOffset": 125,
                        "htmllabels": [
                            "Survival"
                        ],
                        "start": "/p[21]/text()[3]",
                        "startOffset": 1,
                        "text": "However, the obligations of this Agreement shall survive termination for the three (3) year period described in paragraph 3."
                    }
                },
                {
                    "from_name": "ner",
                    "id": "U4eD_TQ614",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/p[24]/text()[2]",
                        "endOffset": 271,
                        "htmllabels": [
                            "Assignment and Succssor"
                        ],
                        "start": "/p[24]/text()[2]",
                        "startOffset": 3,
                        "text": "Neither Party may delegate its obligations hereunder or assign its rights as a Recipient without the prior written consent of the other Party, and any purported assignment or delegation in violation of this Agreement will be void and deemed a breach of this Agreement."
                    }
                },
                {
                    "from_name": "ner",
                    "id": "BwoMq7Bjp3",
                    "to_name": "text",
                    "type": "hypertextlabels",
                    "value": {
                        "end": "/p[25]/text()[2]",
                        "endOffset": 386,
                        "htmllabels": [
                            "Entire Agreement"
                        ],
                        "start": "/p[25]/text()[2]",
                        "startOffset": 0,
                        "text": "Except by a specific written instrument duly executed by both Paties, this Agreement sets forth the entire understanding of the Parties with respect to the subject matter hereof; incorporates and merges any and all previous agreements, understandings, and communications (oral or written) with respect to the subject matter of this Agreement and may not be modified, amended or waived. "
                    }
                }
            ]
        }
    ],
    "data": {
        "filename": "1qpqQsbhhUq.html",
        "text": "<html> html_content </html>"
    },
    "id": 23
}
```


Submit your code in github. Please fix the python version to `3.7`. 
Design and implement the crawler by any framework or packages to get data from Dcard 
(You could leverage Dcard API), and run the crawler within container.

1. 爬取"Apple"版的貼文, 並根據內容尋找合適的Storage進行儲存 
   (Any database (SQL/NoSQL), cloud service would be acceptable), 
   需要的資訊有： 標題, 發文時間, Media URL, `categories`, 內容, `topics`.
2. 需有log file寫出
3. 需要定期6小時進行一次爬取, 並且請勿重複爬取
4. (Optional) 文章如有更新, 設計backfill機制
