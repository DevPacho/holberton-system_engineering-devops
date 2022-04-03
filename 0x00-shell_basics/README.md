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
<ul>
    <li><b>File:</b>&nbsp;<code>0-current_working_directory</code></li>
</ul>
<br>
<h2>1. What&rsquo;s in there?</h2>
<p>Display the contents list of your current directory.</p>
<p>Example:</p>
<pre><code>$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>1-listit</code></li>
</ul>
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
<ul>
    <li><b>File:</b>&nbsp;<code>2-bring_me_home</code></li>
</ul>
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
<ul>
    <li><b>File:</b>&nbsp;<code>3-listfiles</code></li>
</ul>
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
<ul>
    <li><b>File:</b>&nbsp;<code>4-listmorefiles</code></li>
</ul>
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
<ul>
    <li><b>File:</b>&nbsp;<code>5-listfilesdigitonly</code></li>
</ul>
<br>
<h2>6. Welcome</h2>
<p>Create a script that creates a directory named&nbsp;<code>my_first_directory</code> in the&nbsp;<code>/tmp/</code> directory.</p>
<p>Example:</p>
<pre><code>$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
$</code>6-firstdirectory</pre>
<ul>
    <li><b>File:</b>&nbsp;<code></code></li>
</ul>
<br>
<h2>7. Betty in my first directory</h2>
<p>Move the file&nbsp;<code>betty</code> from&nbsp;<code>/tmp/</code> to&nbsp;<code>/tmp/my_first_directory</code>.</p>
<p>Example:</p>
<pre><code>$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>7-movethatfile</code></li>
</ul>
<p><br></p>
<h2>8. Bye bye Betty</h2>
<p>Delete the file&nbsp;<code>betty</code>.</p>
<ul>
    <li>The file&nbsp;<code>betty</code> is in&nbsp;<code>/tmp/my_first_directory</code></li>
</ul>
<p>Example:</p>
<pre><code>$ ./8-firstdelete
$ ls /tmp/my_first_directory/
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>8-firstdelete</code></li>
</ul>
<br>
<h2>9. Bye bye My first directory</h2>
<p>Delete the directory&nbsp;<code>my_first_directory</code> that is in the&nbsp;<code>/tmp</code> directory.</p>
<p>Example:</p>
<pre><code>$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory&apos; (No such file or directory)
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>9-firstdirdeletion</code></li>
</ul>
<p><br></p>
<h2>10. Back to the future</h2>
<p>Write a script that changes the working directory to the previous one.</p>
<pre><code>julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>10-back</code></li>
</ul>
<br>
<h2>11. Lists</h2>
<p>Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the&nbsp;<code>/boot</code> directory (in this order), in long format.&nbsp;</p>
<ul>
    <li><b>File:</b>&nbsp;<code>11-lists</code></li>
</ul>
<br>
<h2>12. File type</h2>
<p>Write a script that prints the type of the file named&nbsp;<code>iamafile</code>. The file&nbsp;<code>iamafile</code> will be in the&nbsp;<code>/tmp</code> directory when we will run your script.</p>
<p>Example</p>
<pre><code>ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
</code></pre>
<p>Note that depending on the file, the output of your script will be different.</p>
<ul>
    <li><b>File:</b>&nbsp;<code>12-file_type</code></li>
</ul>
<br>
<h2>13. We are symbols, and inhabit symbols</h2>
<p>Create a symbolic link to&nbsp;<code>/bin/ls</code>, named&nbsp;<code>__ls__</code>. The symbolic link should be created in the current working directory.</p>
<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>13-symbolic_link</code></li>
</ul>
<br>
<h2>14. Copy HTML files</h2>
<p>Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.</p>
<p>You can consider that all HTML files have the extension&nbsp;<code>.html</code></p>
<ul>
    <li><b>File:</b>&nbsp;<code>14-copy_html</code></li>
</ul>
<br>
<h2>15. Let's move</h2>
<p><b><i>Advanced task</i></b><p>
<p>Create a script that moves all files beginning with an uppercase letter to the directory&nbsp;<code>/tmp/u</code>.</p>
<p>You can assume that the directory&nbsp;<code>/tmp/u</code> will exist when we will run your script</p>
<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 My_file
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Elif_ym
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
ubuntu@ip-172-31-63-244:/tmp/sym$ ./100-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 My_file
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Elif_ym</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>100-lets_move</code></li>
</ul>
<br>
<h2>16. Clean Emacs</h2>
<p><b><i>Advanced task</i></b><p>
<p>Create a script that deletes all files in the current working directory that end with the character&nbsp;<code>~</code>.</p>
<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./101-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>101-clean_emacs</code></li>
</ul>
<br>
<h2>17. Tree</h2>
<p><b><i>Advanced task</i></b><p>
<p>Create a script that creates the directories&nbsp;<code>welcome/</code>,&nbsp;<code>welcome/to/</code> and&nbsp;<code>welcome/to/school</code> in the current directory.</p>
<p>You are only allowed to use two spaces (and lines) in your script, not more.</p>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 102-tree
julien@ubuntu:/tmp/h$ wc -l 102-tree 
2 102-tree
julien@ubuntu:/tmp/h$ head -1 102-tree 
#!/bin/bash
julien@ubuntu:/tmp/h$ tr -cd &apos; &apos; &lt; 102-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
julien@ubuntu:/tmp/h$ ./102-tree 
julien@ubuntu:/tmp/h$ ls
102-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 school
julien@ubuntu:/tmp/h$ </code></pre>
<br>
<h2>18. Life is a series of commas, not periods</h2>
<p><b><i>Advanced task</i></b><p>
<p>Write a command that lists all the files and directories of the current directory, separated by commas (<code>,</code>).</p>
<ul>
    <li>Directory names should end with a slash (<code>/</code>)</li>
    <li>Files and directories starting with a dot (<code>.</code>) should be listed</li>
    <li>The listing should be alpha ordered, except for the directories&nbsp;<code>.</code> and&nbsp;<code>..</code> which should be listed at the very beginning</li>
    <li>Only digits and letters are used to sort; Digits should come first</li>
    <li>You can assume that all the files we will test with will have at least one letter or one digit</li>
    <li>The listing should end with a new line</li>
</ul>
<pre><code>ubuntu@ubuntu:~/$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ubuntu:~/$ ./103-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

ubuntu@ubuntu:~/$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>103-commas</code></li>
</ul>
