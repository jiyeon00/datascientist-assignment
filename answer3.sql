CREATE TABLE answer3(author_id TEXT, yearmonth INTEGER, publication_count INTEGER, citation_count INTEGER)

INSERT INTO answer3(author_id, yearmonth, publication_count, citation_count)
SELECT 
   author_id, yyyymm, count(paper_id), sum(citation_count)
FROM
   (
   SELECT author_id, substr(published_at,1,7) yyyymm, paper_author.paper_id, citation_count
   FROM paper_author
   LEFT OUTER JOIN citation_count_table
   ON paper_author.paper_id = citation_count_table.paper_id
   )
GROUP BY author_id, yyyymm;

SELECT * FROM answer3;
