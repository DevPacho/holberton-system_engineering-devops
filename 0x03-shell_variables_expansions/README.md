<h1>0x03. Shell, init files, variables and expansions</h1>

![image](https://user-images.githubusercontent.com/98773774/165425340-73086dd6-745b-43e0-906e-13c7dc661515.png)

<div>
    <h2>About&nbsp;Bash&nbsp;projects</h2>
    <p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
</div>
<div>
    <h2>Resources</h2>
    <p><strong>Read or watch</strong>:</p>
    <ul>
        <li><a href="https://intranet.hbtn.io/rltoken/G5p7gU70olYFxbN_DfuXpQ" target="_blank" title="Expansions">Expansions</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/C2JAWjeSMt5I0EmuplF32A" target="_blank" title="Shell Arithmetic">Shell Arithmetic</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/zj7i19F9iE9eUdjBgR6C3Q" target="_blank" title="Variables">Variables</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/lHvzUhLmLgBVfsoJzYDj_w" target="_blank" title="Shell initialization files">Shell initialization files</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/5JiNabFuBFXpJKqGGh9EjQ" target="_blank" title="The alias Command">The alias Command</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/lPsbE1Ecs4tmGU2RuTZ5YA" target="_blank" title="Technical Writing">Technical Writing</a></li>
    </ul>
    <p><strong>man or help</strong>:</p>
    <ul>
        <li><code>printenv</code></li>
        <li><code>set</code></li>
        <li><code>unset</code></li>
        <li><code>export</code></li>
        <li><code>alias</code></li>
        <li><code>unalias</code></li>
        <li><code>.</code></li>
        <li><code>source</code></li>
        <li><code>printf</code></li>
    </ul>
    <h2>Learning Objectives</h2>
    <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/73iGFpBHBJtQgO1RmDM-_A" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
    <h3>General</h3>
    <ul>
        <li>What happens when you type&nbsp;<code>$ ls -l *.txt</code></li>
    </ul>
    <h3>Shell Initialization Files</h3>
    <ul>
        <li>What are the&nbsp;<code>/etc/profile</code> file and the&nbsp;<code>/etc/profile.d</code> directory</li>
        <li>What is the&nbsp;<code>~/.bashrc</code> file</li>
    </ul>
    <h3>Variables</h3>
    <ul>
        <li>What is the difference between a local and a global variable</li>
        <li>What is a reserved variable</li>
        <li>How to create, update and delete shell variables</li>
        <li>What are the roles of the following reserved variables: HOME, PATH, PS1</li>
        <li>What are special parameters</li>
        <li>What is the special parameter&nbsp;<code>$?</code>?</li>
    </ul>
    <h3>Expansions</h3>
    <ul>
        <li>What is expansion and how to use them</li>
        <li>What is the difference between single and double quotes and how to use them properly</li>
        <li>How to do command substitution with&nbsp;<code>$()</code> and backticks</li>
    </ul>
    <h3>Shell Arithmetic</h3>
    <ul>
        <li>How to perform arithmetic operations with the shell</li>
    </ul>
    <h3>The&nbsp;<code>alias</code> Command</h3>
    <ul>
        <li>How to create an alias</li>
        <li>How to list aliases</li>
        <li>How to temporarily disable an alias</li>
    </ul>
    <h3>Other&nbsp;<code>help</code> pages</h3>
    <ul>
        <li>How to execute commands from a file in the current shell</li>
    </ul>
    <h2>Requirements</h2>
    <h3>General</h3>
    <ul>
        <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
        <li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
        <li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
        <li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
        <li>The first line of all your files should be exactly&nbsp;<code>#!/bin/bash</code></li>
        <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, describing what each script is doing</li>
        <li>You are not allowed to use&nbsp;<code>&amp;&amp;</code>,&nbsp;<code>||</code> or&nbsp;<code>;</code></li>
        <li>You are not allowed to use&nbsp;<code>bc</code>,&nbsp;<code>sed</code> or&nbsp;<code>awk</code></li>
        <li>All your files must be executable</li>
    </ul>
    <h2>More Info</h2>
    <p>Read your&nbsp;<code>/etc/profile</code>,&nbsp;<code>/etc/inputrc</code> and&nbsp;<code>~/.bashrc</code> files.</p>
    <p>Look at some files in the&nbsp;<code>/etc/profile.d</code> directory.</p>
    <p>Note: You do not have to learn about&nbsp;<code>awk</code>,&nbsp;<code>tar</code>,&nbsp;<code>bzip2</code>,&nbsp;<code>date</code>,&nbsp;<code>scp</code>,&nbsp;<code>ulimit</code>,&nbsp;<code>umask</code>, or shell scripting, yet.</p>
<br>
  
<h1>Tasks</h1>
<h2>0. "o"</h2>
   
