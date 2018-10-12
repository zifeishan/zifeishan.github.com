Projects
====

----

## Stanford Course Projects

Here are some fun course projects I led during Master's studies, along
with the reports and posters. Some of these projects might be
interesting enough for industry reference.


<h3 id="ensemble-ocr">Ensemble Optical Character Recognition (OCR) Systems</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/ensemble-ocr.png}}"><img class="" title="" src="{{ref:images/ensemble-ocr.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p>This is the course project for Stanford CS229 Machine Learning, and independent study with Professor Christopher Re. I was the main contributor of this project.</p>
            <p>We studied the problem of Optical Character Recognition on domain-specific articles (geo-science papers), and found that multiple OCR systems often make independent errors that can be fixed by each other. We implemented an offline Machine Learning model (SVM) to predict the correct output when the two OCR systems differ. This combines two state-of-the-art OCR systems at the time, <em>Tesseract</em> and <em>Cuneiform</em>. For error examples, Tesseract would often recognize <code>rn</code> as <code>m</code>, and Cuneiform would often recognize <code>e</code> as <code>c</code>.  Our ensemble system was able to choose the correct answer in most cases, and achieves 89.80% accuracy when two OCR differs and one of them is correct, yielding a significant accuracy increase to any single OCR system involved.</p>
            <p>Report: [<a href="/files/ensemble-ocr.pdf">PDF</a>]</p>
        </div>
    </div>
</div>

<h3 id="capital-crunch">Capital Crunch: Predicting Investments in Tech Companies</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/capital-crunch.png}}"><img class="" title="" src="{{ref:images/capital-crunch.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p>Capital Crunch is our efforts to predict investments happening between investors and technology startups. We used data from <a href="http://www.crunchbase.com/">CrunchBase</a>, built Logistic Regression and CRF models, used linguistic features and social indicators. We achieved around 80% precision based on our heuristic evaluation methods.
            </p>
            <p>Report: [<a href="/files/capital-crunch.pdf">PDF</a>]</p>
            <p>Poster: [<a href="/files/capital-crunch-poster.pdf">PDF</a>]
            <p>Code: [<a href="https://github.com/zifeishan/capital-crunch">GitHub</a>]
        </div>
    </div>
</div>


<h3 id="kaleidoscope">Kaleidoscope</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="/kaleidoscope"><img class="" title="" src="{{ref:images/kaleidoscope.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p><a href="/kaleidoscope">Kaleidoscope</a> is an interactive ideation system, assisting humans in the brainstorming by automatically suggesting new ideas. It will record user's ideas into system's backend idea networks, and make suggestions that are relavent, diverse, and inspiring.</p>
            <p>Report: [<a href="/files/kaleidoscope.pdf">PDF</a>]</p>
            <p>Poster: [<a href="/files/kaleidoscope-poster.pdf">PDF</a>]
        </div>
    </div>
</div>

<h3 id="deepspeech">DeepSpeech: A Scalable Decoding System that Integrates Knowledge for Speech Recognition</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/deepspeech.png}}"><img class="" title="" src="{{ref:images/deepspeech.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p>DeepSpeech is a project that uses DeepDive to decode the word lattice in speech recognition. It is able to integrate various features, and do probabilistic inference to choose a best path of words to output.
            </p>
            <p>Report: [<a href="/files/deepspeech.pdf">PDF</a>]</p>
            <p>Poster: [<a href="/files/deepspeech-poster.pdf">PDF</a>]
            <p>Code: [<a href="https://github.com/zifeishan/cs224s-deepSpeech">GitHub</a>]
        </div>
    </div>
</div>

<h3 id="authorship_attribution">Authorship Attribution in multi-author documents</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/authorship_attribution.png}}"><img class="" title="" src="{{ref:images/authorship_attribution.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p>Collaborative project with Tim Althoff and Denny Britz.
            </p>
            <p>We bring up a novel problem of identifying the authors of scientific publications in a multi-author setting. Initial results show that writing styles can be used to predict authors with significant accuracy. This challenges the assumption that simply removing names from a paper submission ensures anonymity in a double-blind process.
            </p>
            <p>Report: [<a href="/files/authorship_attribution.pdf">PDF</a>]</p>
            <p>Slides: [<a href="/files/authorship_attribution_slides.pdf">PDF</a>]</p>
        </div>
    </div>
</div>


----

## Previous Projects

<h3 id="mlbi">MLB illustrator</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/mlbi_large.png}}"><img class="" title="" src="{{ref:images/mlbi_large.png}}" /></a>
        </div></div>
        <div class="col-md-9">
            <p><a href="http://www.zifeishan.org/mlb_illustrator/">MLB illustrator</a> is a project visualizing the MLB game data as a heterogeneous network, providing baseball statistics, and ranking the batting and pitching ability of players.</p>
            <p>Based on this project, I conducted independent research, and raised GameRank---a ranking algorithm for networks with multiple interplaying indicators.</p>
        </div>
    </div>
</div>


<h3 id="beijing3ds">Beijing 3DS Website</h3>


<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/bj3ds.png}}"><img class="" title="" src="{{ref:images/bj3ds.png}}" /></a>
        </div></div>
        <div class="col-md-9">


Beijing 3DS is an international startup competition held in Beijing. </p>
<p>I am the back-end designer of the event website. I mainly built NGINX server and application form handler, and successfully processed all the applications for the event.</p>
        </div>
    </div>
</div>

<h3 id="qa">Question answering system on Chinese Wikipedia</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/chinesewiki.png}}"><img class="" title="" src="{{ref:images/chinesewiki.png}}" /></a>
        </div></div>
        <div class="col-md-9">

<p>Team leader; designed QA algorithm using Chinese NLP techniques.</p>
        </div>
    </div>
</div>

<h3 id="wordnet">WordNet viewer featuring force-driven graph of words</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/wordnet.png}}"><img class="" title="" src="{{ref:images/wordnet.png}}" /></a>
        </div></div>
        <div class="col-md-9">


<p>Designed the dynamic relationship graph with an originated force-driven layout algorithm.</p>
        </div>
    </div>
</div>

<h3 id="game">2D Shooting Game programmed with Haaf’s Game Engine</h3>

<div class="row">
    <div class="col-md-12">
        <div class="col-md-3">
            <div class="thumbnail">
            <a href="{{ref:images/2dgame.png}}"><img class="" title="" src="{{ref:images/2dgame.png}}" /></a>
        </div></div>
        <div class="col-md-9">
<p>Sole developer; used C++ OO programming; designed barrages with a force model.</p>
        </div>
    </div>
</div>


### Minijava compiler for Android

Worked on optimization; realized general optimizations based on dafaflow analysis.

### Kademlia network distributed simulation

Team leader; implemented a UDP-based P2P network using Kademlia DHT.

### AI for game “Blokus” generated by Genetic Algorithm

Designed game AI; used GA to refine arguments for AI; ranked top 20% in department.
