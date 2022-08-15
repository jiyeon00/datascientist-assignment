-- ANSWER 4
CREATE TABLE answer4 (author_id TEXT, hindex INTEGER)

INSERT INTO answer4(author_id, hindex)
SELECT author_id, min(ValRank) hindex
FROM
   (SELECT 
      *, 
      RANK () OVER ( 
         ORDER BY citation_count DESC
      ) ValRank
   FROM
      (
      SELECT author_id, substr(published_at,1,7) yyyymm, paper_author.paper_id, citation_count
      FROM paper_author
      LEFT OUTER JOIN citation_count_table
      ON paper_author.paper_id = citation_count_table.paper_id
      )
   WHERE author_id = 'a31')
WHERE citation_count <= ValRank
;
