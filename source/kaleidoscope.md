Kaleidoscope
====

**Kaleidoscope** is an interactive ideation system, assisting humans in the brainstorming by automatically **suggesting new ideas**. It will record user's ideas, search its knowledge base, and make suggestions that are relavent, diverse, and inspiring.

System in action
----

<div class="row">
    <div class="col-md-12">
        <div class="col-md-6">
            <div class="thumbnail">
            <a href="{{ref:images/kaleido-2.png}}"><img class="" title="" src="{{ref:images/kaleido-2.png}}" /></a>
        </div></div>
        <div class="col-md-6">
            <div class="thumbnail">
            <a href="{{ref:images/kaleido-3.png}}"><img class="" title="" src="{{ref:images/kaleido-3.png}}" /></a>
        </div></div>        
    </div>
</div>


[Try it now!](http://54.201.132.108:3000/)
----

Although our system is only in testing phase, you are more than welcome to try it out. 

Please help us with your feedback, by clicking "like" or "dislike" to ideas suggested by the system.

NOTE: since preparing for the suggestions are currently slow, please wait for the suggestions to pop up. Do not click "Brainstorm" button for multiple times!

You can use the following account (or your own account if you have one):

- Username: test
- Password: 45658
- Be sure to click "RESET" before you start.

Enter the platform [HERE](http://54.201.132.108:3000/)!

NOTE 2: Now we only have a single-threaded backend without a message queue. If your request is lost, please try sending again.


How it works
----

“Ideation” is an essential process in creativity and problem-solving.
Golden rules in brainstorming include: “ideas build on each other”,
“defer judgment”, “seek quantity and diversity”. Following these rules,
we develop a novel approach to assisting human brainstorming by idea
recommendation.

We construct idea networks from heterogeneous datasets, define
objectives to recommend ideas, design algorithms to achieve these
objectives, and craft a working, interactive brainstorming system.

Our backend idea networks use following datasets:

- [DBPedia](dbpedia.org/Datasets), an open dataset of Wikipedia.
- [ConceptNet](conceptnet5.media.mit.edu), a knowledge networks of concepts.
- [MIRFLICKR](press.liacs.nl/mirflickr/), an open image collection of 25,000 Flicker images.


Authors
----

- [Zifei Shan](http://www.zifeishan.org)
- [Yuke Zhu](http://www.stanford.edu/~yukez)
- Tianxin Zhao

Also see [Sparkl](http://sparkl.us/)!
----

Sparkl is our great buddy, a web platform that empowers collaborative creative thinking
by facilitating virtual synchronous brainstorming.


