-- ANSWER 5
CREATE TABLE answer5(author_id TEXT, h5index INTEGER);

INSERT INTO answer5(author_id, h5index)
SELECT author_id, 
   CASE WHEN(citation_count < ValRank) THEN min(ValRank)-1 ELSE min(ValRank) END hindex
FROM
   (SELECT 
      *,
      RANK () OVER ( 
         ORDER BY citation_count DESC
      ) ValRank
   FROM
      (
      SELECT author_id, substr(published_at,1,4) yyyy, paper_author.paper_id, citation_count
      FROM paper_author
      LEFT OUTER JOIN citation_count_table
      ON paper_author.paper_id = citation_count_table.paper_id
      WHERE author_id = 'a32'
      )
   WHERE CAST(yyyy AS INTEGER) <= 2021 and CAST(yyyy AS INTEGER) >= 2017)
WHERE citation_count <= ValRank;
