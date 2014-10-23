To run the crawler and rank clusters of wikipedia pages naively:
python crawler.py

To run the crawler that ranks wikipedia pages using pagerank:
python PageRankCrawler.py

To get the distance metrics from the run of crawler:
python bhattacharyya.py 

Results comparing each distribution pairwise will be in
bhattacharyyadistance.txt

Average Bhattacharyya distance and K-L divergence of the distributions will be
listed at the bottom of this file.

The data collected from the crawler run will be in data.txt
The data collected from the PageRankCrawler will be in page_rank_data.txt
*NOTE: PageRankCrawler takes a very large amount of time to get any results.
