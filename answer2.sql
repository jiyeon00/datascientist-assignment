CREATE TABLE answer2(author_id TEXT, year INTEGER ,publication_count INTEGER, citation_count INTEGER);

INSERT INTO answer2(author_id, year, publication_count, citation_count)
SELECT 
   author_id, cast(yyyy as integer) yyyy, count(paper_id) , sum(citation_count)
FROM
   (
   SELECT author_id, substr(published_at,1,4) yyyy, paper_author.paper_id, citation_count
   FROM paper_author
   LEFT OUTER JOIN citation_count_table
   ON paper_author.paper_id = citation_count_table.paper_id
   )
GROUP BY author_id , yyyy ;

SELECT * FROM answer2;
