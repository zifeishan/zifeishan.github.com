<!-- 
My Research
====

The explosion of data provides us computer scientists a unique
opportunity for understanding the dynamics of the world --- knowledge
that has the potential to impact society. I am intrigued by the union
of data mining and information networks to answer fundamental
questions: How do large networks evolve? How do we better understand
large-scale human interactions? How are networks made robust to
unexpected behavior?

I have explored some of these questions during my undergraduate
studies. I led an independent research project to automatically rank
players in a baseball network. In a series of studies, I investigated
real-world phenomena using large-scale data provided by Renren, a
massive Chinese social network. Specifically, I led a project devising
defenses against profile-cloning attacks. I further collaborated on a
separate study on Sybil-attack detection. Finally, I was involved in
assessing the impact of user-interaction transparency on their
behavior.
 -->

Research Groups
====

During my master's studies at Stanford, I have the honor to work with
Professor [Christopher Ré](http://cs.stanford.edu/people/chrismre/)
and get inspired by other great minds in InfoLab.  I work on projects
in Knowledge Base Construction (KBC), the process of populating
relational databases with information extracted from data.  I develop
[DeepDive](http://deepdive.stanford.edu/), a data management tool that
is powerful for KBC. Through these experiences, I discovered how
systematic research methods boost industrial applications, and how
engineering tasks facilitate research projects.

I will be a research intern in Knowledge Base Group of 
[Toshiba Corporation](http://www.toshiba.co.jp/worldwide/), from Jan 2015 to Mar 2015.

I was in [Computer Networks and Distributed Systems Lab](http://net.pku.edu.cn/p2p/doku.php) of Peking University, advised by professor [Yafei Dai](http://cn.linkedin.com/pub/yafei-dai/9/291/b1). I mainly work with Dr. Jing Jiang on Online Social Networks.

I was one of the co-leaders of "Universal UI" research group, advised by Prof. [Daniel A. Freedman](http://www.danielfreedman.org/). My team members are: [Scott Cheng](http://scottcheng.com/), [Haoyu Zhang](http://www.haoyuzhang.org/), Chris (Xiuhan) Hu, and Chen Yu.

I was on the "Technion-Peking Research Exchange Program", together with seven other PKU students: Annie Liu, [Haoyu Zhang](http://www.haoyuzhang.org), Zhao Yang, [Yilun Zhang](http://www.yilunzhang.com), Michelle Ma, Jason Lv, and Winnie Liu. 

<!-- Independent research -->

Recent Projects
====

## DeepDive

<div class="row" id="deepdive">
<div class="col-md-12">
<div class="col-md-3">
<div class="thumbnail">
<a href="http://deepdive.stanford.edu/">
<img class="" title="" src="{{ref:images/deepdive-square.png}}" />
</a>
</div>
</div>
<div class="col-md-9" markdown=1>

<a href="http://deepdive.stanford.edu/">DeepDive</a>
is a generic probabilistic inference engine that uses
declarative languages to specify factor graphs, and performs scalable
learning and inference. It is most widely used for the task of KBC. I
made significant contribution to the DeepDive code base, and see my
infrastructural efforts actually facilitate research projects in
group. My efforts include:

<ol>
<li>
<emph>Contributed to DeepDive's feature extraction pipelines.</emph> DeepDive
features a pipeline that enables flexible parallel feature
extraction.
This pipeline is vitally important and widely used in all our
applications, but it suffered from unsatisfactory speed. I
researched into the problem, and found that
the parallel task scheduler, data loader and unloader were the
bottlenecks. I implemented two faster code paths to solve this issue:
one code path uses the system tool "xargs" to manage parallelism, and
optimized loading and dumping of the database; the other code path
compiles user's extraction script to 
a database procedural language,
to further reduce disk I/Os by running the UDF in database.
These implementations turned out to be 10x--20x faster than the
original one, and unblocked many large-scale research projects.
</li>
<li>
<emph>Ported DeepDive from PostgreSQL into 
<a href="http://deepdive.stanford.edu/doc/advanced/mysql.html">MySQL, MariaDB, and MySQL cluster</a>
,</emph> to extend its usability. 
I also refactored the code base for easier
integration with other DBMS. A challenge occurred that our 
newly-supported distributed DBMS, MySQL cluster, suffers from slow data
loading with DeepDive. To tackle this problem, I implemented a faster
loader for DeepDive using APIs provided by MySQL cluster.
</li>
<li>
<emph>Working on an interactive KBC tool that automates feature engineering</emph>.
The systematic way of feature engineering in KBC has been proposed,
but not well automated by DeepDive. I am working on <a href="https://github.com/zifeishan/braindump">a tool named BrainDump</a> to
automatically generate reports to summarize each run of DeepDive and
auto-detect possible failure modes.
I am also working on the visualization of end
products for KBC, to automatically serve the generated knowledge base
online, with various ways to interact with users.
</li>
</ol>
</div>
</div>
</div>



## Public Scientific Knowledge Base

<div class="row" id="plos">
<div class="col-md-12">
<div class="col-md-3">
<div class="thumbnail">
<a href="{{ref:images/plos.png}}">
<img class="" title="" src="{{ref:images/plos_thumb.png}}" />
</a>
</div>
</div>
<div class="col-md-9" markdown=1>

<p>I am building an open knowledge base for 
<a href="http://www.plos.org/">Public Library of Science (PLOS)</a>,
which integrates scientific entities and relations extracted by DeepDive. The knowledge base will be released <a href="http://plosdeepdive.stanford.edu/">HERE</a>.
</p>

<p>
	The demo to the left shows the view of our interface, where all scientific entity and relation mentions (genes and phenotypes) are highlighted in the paper, and you can easily view top genes and phenotypes in this paper with a summary on the left column. You will be also able to provide feedback on whether each extracted mention is correct, by using the tagging interface to the right.
</p>
</div>
</div>
</div>


Previous Research Projects
====

Ranking and analyzing baseball network
----
<div class="row" id="gamerank">
<div class="col-md-12">
<div class="col-md-3">
<div class="thumbnail">
<p><img class="" title="" src="{{ref:images/gamerank_thumb.png}}" /></p>
</div>
<div class="thumbnail">
<p><img class="" title="" src="{{ref:images/mlbi.jpg}}" /></p></div>
</div>
<div class="col-md-9" markdown=1>

<p>This was my course project for 
<a href="http://open.umich.edu/education/si/si508/fall2008">SI 508---Networks: Theory and Application</a>, 
given by Prof. <a href="http://www-personal.umich.edu/~qmei/">Qiaozhu Mei</a> from UMich.
The project
originates from my idea to regard American Major League Baseball (MLB,
of which I am a big fan) games as a network, with players as nodes and
their win-lose conditions in games as links.
</p>
<p>To rank the players in the network, we first tried PageRank, but it
failed to describe a special attribute of the network: a pitcher who
defeats good batters is a great pitcher, and a batter who wins skilled
pitchers is an awesome batter. Faced with this obstacle, I used the
intuition in HITS algorithm (with hubs and authorities) to modify
PageRank, and raised a new random walk algorithm to measure the two
abilities. Our next problem was to evaluate our algorithm, when there
are no definite criteria to judge baseball rankings. Therefore I
compared our results to a prestige ranking system named ESPN Ratings,
and the plots show that we achieve similar results with ESPN while
having a simpler model and a wider capability.</p>
<p>In the data-mining
phase, I studied the network over time, and found interesting 
patterns that recent players are getting closer in their skills than before, 
and good pitchers are better than ordinary pitchers at batting.</p>

<!-- <p>In short, I enjoy this research because it involves understanding
social networks, their evolution, and their application to human
activities. 
As a future project, I might try to investigate
heterogeneous baseball networks involving both players and teams as
different types of nodes, to revise the ranking algorithm,
explore their evolution,
and test the robustness of each team based on data of in-team 
supports, to see whether the team is too dependent on certain players. 
Further research might lead to brand new strategies in real games.</p>
 -->
<p>Paper: [<a href="/files/gamerank_zifeishan.pdf">PDF</a>]</p>
<p>Slides: [<a href="/files/gamerank_slides_zifei.pptx">PPTX</a>] [<a href="/files/gamerank_slides_zifei.pdf">PDF</a>]</p>

</div>
</div>
</div>


Defending against cloning attacks in OSNs
----
<div class="row" id="cloning">
<div class="col-md-12">
<div class="col-md-3">
<div class="thumbnail">
<img class="" title="" src="{{ref:images/cloning_thumb.png}}" />
</div></div>
<div class="col-md-9" markdown=1>

<p>My other independent research is about defending against cloning
attacks in Online Social Networks (OSNs). Cloning attackers disguise
fake accounts as existing users by copying
their profiles, and send requests to the friends of the cloned victim.
This project is motivated by my long time interest in making OSNs more
robust, and by my coincidental encounter with a cloning attack while
using Renren (a Facebook-style OSN in China).  I conducted a
literature search and found that although earlier studies described
this attack pattern, it cannot be adopted for large-scale attacks, and
they did not provide a method for defending against it. So I first
improved the attack pattern by snowball sampling (adding cheated
people's friend) and iteration attack (cloning cheated people's
friend), to point out its potential threats. Secondly we tested
its feasibility on Renren. Then I came up with a simple but
powerful server-side defending system by IP sequence matching. I also
notice that the defending strategy is fragile to IP spoofing, so in the
future I'd like to study stronger metrics of account identity, like
clicking pattern matching and action time similarity.</p>

<p>Paper: [<a href="http://delivery.acm.org/10.1145/2450000/2448615/a59-shan.pdf?ip=162.105.91.67&acc=ACTIVE%20SERVICE&CFID=304062296&CFTOKEN=69551978&__acm__=1364440771_3b01294c1ce3b4a4160d30d888aa3796">PDF</a>]</p>
<p>Slides: [<a href="/files/cloning_slides_zifei.pptx">PPTX</a>]</p>

</div>
</div>
</div>



Detecting Sybil groups in OSNs
----

<div class="row" id="sybil">
<div class="col-md-12">
<div class="col-md-3">
<div class="thumbnail">
<img class="" title="" src="{{ref:images/sybil_thumb.png}}" />
</div></div>
<div class="col-md-9" markdown=1>

<p>My major research project advised by Professor Yafei Dai in her Lab
is to detect Sybil Attack groups in OSNs. Sybil Attackers manipulate
multiple accounts to increase the attacker's power. We aimed at
detecting Sybil attacks in the wild, in cooperation with Renren---the
"Facebook in China" with over 200 million users. I worked with Jing
Jiang, a graduate student in our lab. Our paper is published in ICDCSW
'12, and JCST. In the project, I
coded all the programs in all phases from scratch, implemented
efficient algorithms to handle the graph with millions of nodes, and
designed many measurements based on discussion with Jing.</p>

<!-- <p>One special experience to me is in the evaluation phase, where I raised
and revised an indicator. We wanted to verify that the detected Sybil
groups are controlled by attackers, which matches my interest in
uncovering human behaviors behind the action pattern. We assumed that
among users in a group, the more similar their "action times" are, the
more likely they are manipulated. In order to quantify the "similarity"
of time points inside a group, I raised a new method: I sorted all the
points on the timeline, calculated the differences between adjacent
points, and got the median of all those differences, which is M.
However, I found that M was not a good indicator since it is
correlated with the number of time points N, illustrated by the
M-N log-log scatter diagram of random user groups. I explained this
phenomenon by intuition: as the length of the timeline is limited, the
more points there are, the more closely they are distributed onto the
timeline, and the smaller M it has. So I used MN as the new
indicator, and the diagram shows that the value is unrelated with N.</p>
 -->

<!-- <p>In the measurement phase, I mined the network and discovered lots of
knowledge.  Therein I enjoy the study of "group
merging pattern", inspired by an interest on evolutions of real-world
Sybil groups. I spotted that sometimes two connected components merge
into one, and I wanted to compare the difference between Sybil groups
and normal users in merging pattern. By making tables counting the size
of two components when they merge, I found that in Sybil groups,
"one-to-many merging" is the major pattern, and "many-to-many merging"
is far rarer than in normal groups, which indicates that Sybil groups
lack variety in merging pattern, with a majority of joining a new
account into an existing component. The result improves my interest in
network dynamics. </p>
 -->

<p>Paper: [<a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6258146">PDF</a>]</p>
</div></div></div>

Assessing the Impact of User-interaction Transparency in Social Networks
----
I was involved in another project at lab, to understand latent user
interactions, working with Jing Jiang advised by Professor Dai. In
OSNs, profile browsing, which is latent to third-parties, are actually
the most prevalent type of user interactions. Supported with the
dataset provided by Renren, we compared this latent network with
visible one of comments and retweets, based on the dataset provided by
Renren. My work involved measuring structural properties including
conductance, modularity and mixing time, for both visible and latent
graphs. I enjoyed this research, in the process of understanding
characteristics of different networks in the wild, and quantifying the
human interactions. As a future question, it will be very attractive
for me to compare the dynamics of latent and visible networks,
especially their information diffusion, to discover how the hot topics
and rumors spread among users.

<!-- Other research -->

Research Exchange Program at Technion
----
In Fall 2012 I joined a research exchange program at Technion, advised
by Professor Daniel Freedman. At Technion I took advanced graduate
courses, including seminars in Reliable Distributed Computing by Prof.
Idit Keidar, and Program Analysis and Synthesis by Prof. Eran Yahav. I
am also engaging in academic activities at Technion, being exposed to
lectures and colloquiums on a wide range of topics in Computer Science,
given by international researchers. Most importantly, I explored new research directions as part of a vibrant group. Our topics cover
Programming Language, Systems, and Human Computer Interaction. We
design description languages to automate the creation of both front-end
and back-end systems, and discover human behavior
patterns in interacting with services. 
