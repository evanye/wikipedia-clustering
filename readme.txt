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

To run the visualization of feature vectors:
python visualize

To run the visualization using the Bhattacharyya distance matrix:
python visualize --dist-matrix

*NOTE: visualize may require some external python libraries to run. Furthermore, visualize without --dist-matrix only works on linux; it uses the tSNE binary, and I have only included the linux version of it. visualize --dist-matrix, however, uses a python implementation of tSNE, so I believe it is platform independent. 
