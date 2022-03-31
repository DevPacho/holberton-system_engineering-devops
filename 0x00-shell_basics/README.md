<h1>0x00. Shell, basics</h1>
<h2>About Bash projects</h2>
<p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
<p></p>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg">
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/pn2_LGNuA1yFY7zy3CQmig" target="_blank" title='What Is "The Shell"?'>What Is &ldquo;The Shell&rdquo;?</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Hh8elGgCpj--6othR7S7GQ" target="_blank" title="Navigation">Navigation</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/84xsZOempqy5I7ZkueeIsg" target="_blank" title="Looking Around">Looking Around</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Jp1c4V3hJiGBuVzYCtnQKw" target="_blank" title="A Guided Tour">A Guided Tour</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/wFwFXKQmSpmxYyvHvCIC-Q" target="_blank" title="Manipulating Files">Manipulating Files</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Aq3NVLBhgnQS6NYtHI8i4w" target="_blank" title="Working With Commands">Working With Commands</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/RohkjGiQtMHgPfj0N_k1Bw" target="_blank" title="Reading Man pages">Reading Man pages</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/0HvJ2B_wSl6Oyshcn-OHrg" target="_blank" title="Keyboard shortcuts for Bash">Keyboard shortcuts for Bash</a></li>
    <li><a href="https://wiki.ubuntu.com/LTS" target="_blank">LTS</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/ketzZf-802Fb-mSGkyPa4w" target="_blank" title="Shebang">Shebang</a></li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
    <li><code>cd</code></li>
    <li><code>ls</code></li>
    <li><code>pwd</code></li>
    <li><code>less</code></li>
    <li><code>file</code></li>
    <li><code>ln</code></li>
    <li><code>cp</code></li>
    <li><code>mv</code></li>
    <li><code>rm</code></li>
    <li><code>mkdir</code></li>
    <li><code>type</code></li>
    <li><code>which</code></li>
    <li><code>help</code></li>
    <li><code>man</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/uzS14i1TrIOzP984RDR4-Q" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>What does RTFM mean?</li>
    <li>What is a Shebang</li>
</ul>
<h3>What is the Shell</h3>
<ul>
    <li>What is the shell</li>
    <li>What is the difference between a terminal and a shell</li>
    <li>What is the shell prompt</li>
    <li>How to use the history (the basics)</li>
</ul>
<h3>Navigation</h3>
<ul>
    <li>What do the commands or built-ins&nbsp;<code>cd</code>,&nbsp;<code>pwd</code>,&nbsp;<code>ls</code> do</li>
    <li>How to navigate the filesystem</li>
    <li>What are the . and .. directories</li>
    <li>What is the working directory, how to print it and how to change it</li>
    <li>What is the root directory</li>
    <li>What is the home directory, and how to go there</li>
    <li>What is the difference between the root directory and the home directory of the user root</li>
    <li>What are the characteristics of hidden files and how to list them</li>
    <li>What does the command&nbsp;<code>cd -</code> do</li>
</ul>
<h3>Looking Around</h3>
<ul>
    <li>What do the commands&nbsp;<code>ls</code>,&nbsp;<code>less</code>,&nbsp;<code>file</code> do</li>
    <li>How do you use options and arguments with commands</li>
    <li>Understand the ls long format and how to display it</li>
    <li><a href="https://intranet.hbtn.io/rltoken/Jp1c4V3hJiGBuVzYCtnQKw" target="_blank" title="A Guided Tour">A Guided Tour</a></li>
    <li>What does the&nbsp;<code>ln</code> command do</li>
    <li>What do you find in the most common/important directories</li>
    <li>What is a symbolic link</li>
    <li>What is a hard link</li>
    <li>What is the difference between a hard link and a symbolic link</li>
</ul>
<h3>Manipulating Files</h3>
<ul>
    <li>What do the commands&nbsp;<code>cp</code>,&nbsp;<code>mv</code>,&nbsp;<code>rm</code>,&nbsp;<code>mkdir</code> do</li>
    <li>What are wildcards and how do they work</li>
    <li>How to use wildcards</li>
</ul>
<h3>Working with Commands</h3>
<ul>
    <li>What do&nbsp;<code>type</code>,&nbsp;<code>which</code>,&nbsp;<code>help</code>,&nbsp;<code>man</code> commands do</li>
    <li>What are the different kinds of commands</li>
    <li>What is an alias</li>
    <li>When do you use the command help instead of man</li>
</ul>
<h3>Reading Man Pages</h3>
<ul>
    <li>How to read a man page</li>
    <li>What are man page sections</li>
    <li>What are the section numbers for User commands, System calls and Library functions</li>
</ul>
<h3>Keyboard Shortcuts for Bash</h3>
<ul>
    <li>Common shortcuts for Bash</li>
</ul>
<h3>LTS</h3>
<ul>
    <li>What does&nbsp;<code>LTS</code> mean?</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
    <li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
    <li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/bin/bash</code></li>
    <li>A&nbsp;<code>README.md</code> file at the root of the repo, containing a description of the repository</li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of&nbsp;<em>this</em> project, describing what each script is doing</li>
    <li>You are not allowed to use backticks,&nbsp;<code>&amp;&amp;</code>,&nbsp;<code>||</code> or&nbsp;<code>;</code></li>
    <li>All your scripts must be executable. To make your file executable, use the&nbsp;<code>chmod</code> command:&nbsp;<code>chmod u+x file</code>. Later, we&rsquo;ll learn more about how to utilize this command.</li>
</ul>
<h2>More Info</h2>
<p><em>Example of line count and first line</em></p>
<pre><code>julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
#!/bin/bash
julien@ubuntu:/tmp$ 
</code></pre>
<p>In order to test your scripts, you will need to use this command:&nbsp;<code>chmod u+x file</code>. We will see later what does&nbsp;<code>chmod</code> mean and do, but you can have a look at&nbsp;<code>man chmod</code> if you are curious.</p>
<p><em>Example</em></p>
<pre><code>julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$ </code></pre>
<br>
<h1>Tasks</h1>
<h2>0. Where am I?</h2>
<p>Write a script that prints the absolute path name of the current working directory.</p>
<p>Example:</p>
<pre><code>$ ./0-current_working_directory
/0x00-shell_basics
$</code></pre>
<br>
<h2>1. What&rsquo;s in there?</h2>
<p>Display the contents list of your current directory.</p>
<p>Example:</p>
<pre><code>$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$</code></pre>
<br>
<h2>2. There is no place like home</h2>
<p>Write a script that changes the working directory to the user&rsquo;s home directory.</p>
<ul>
    <li>You are not allowed to use any shell variables</li>
</ul>
<pre><code>julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$ </code></pre>
<br>
<h2>3. The long format</h2>
<p>Display current directory contents in a long format</p>
<p>Example:</p>
<pre><code>$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$</code></pre>
<br>
<h2>4. Hidden files</h2>
<p>Display current directory contents, including hidden files (starting with&nbsp;<code>.</code>). Use the long format.</p>
<p>Example:</p>
<pre><code>$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$</code></pre>
<br>
<h2>5. I love numbers</h2>
<p>Display current directory contents.</p>
<ul>
    <li>Long format</li>
    <li>with user and group IDs displayed numerically</li>
    <li>And hidden files (starting with .)</li>
</ul>
<p>Example:</p>
<pre><code>$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$</code></pre>
<br>
<h2>6. Welcome</h2>
<p>Create a script that creates a directory named&nbsp;<code>my_first_directory</code> in the&nbsp;<code>/tmp/</code> directory.</p>
<p>Example:</p>
<pre><code>$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
$</code></pre>
<br>
