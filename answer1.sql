CREATE TABLE citation_count_table(paper_id TEXT, citation_count INTEGER);

INSERT INTO citation_count_table(paper_id, citation_count)
SELECT 
   reference_paper_id, count(*) 
FROM 
   paper_reference 
GROUP BY reference_paper_id;


CREATE TABLE answer1(author_id TEXT,publication_count INTEGER, citation_count INTEGER);

INSERT INTO answer1(author_id, publication_count, citation_count)
SELECT author_id, count(paper_id), sum(citation_count)
FROM
   (
   SELECT *
   FROM paper_author 
   LEFT OUTER JOIN citation_count_table
   ON paper_author.paper_id = citation_count_table.paper_id
   )
GROUP BY author_id;

SELECT * FROM answer1;
