# EasyCrawler

The most basic and simple Python crawler example, suitable for beginners to understand the working principle and implementation of the crawler, and add functions on this basis.

The basic functions of the crawler are as follows:

-After entering an entry address, it will crawl the page pointed to by `href =` in the address webpage, download the content, and save it in turn
-Bad links that cannot be accessed will be ignored
-The crawler can only crawl the link to the entrance address, no longer crawling deeper
-Will automatically code the page ID and skip the crawled pages

The entire example rarely relies on external projects and is very simple, easy to understand, and pure. Therefore, the project is not only easy to learn, but also easy to expand and modify on this basis.

Based on the above functions, we can modify and implement many other functions, including but not limited to:

-Continue crawling based on the page instead of crawling only one layer of links
-Set crawling scope, for example, crawl only links under a certain domain name
-Regularly crawl the data of an address and compare its changes
-Only crawl the picture information in the web page
- and many more……