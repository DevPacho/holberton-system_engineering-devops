<h1>0x02. Shell, I/O Redirections and filters</h1>
<img src="https://www.linuxunit.com/images/stdin-stdout-stderr.png">
<p>©. <a href="https://www.linuxunit.com/io-redirection-stdin-stdout-stderr-streams/" target="_blank"><i><b>Image source</a></i></b></p>
<br>
<div>
    <h2>About&nbsp;Bash&nbsp;projects</h2>
    <p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
</div>
<div>
    <h2>Resources</h2>
    <p><strong>Read or watch</strong>:</p>
    <ul>
        <li><a href="https://intranet.hbtn.io/rltoken/Kwe7oA6N7iWf8kfnteJLrA" target="_blank" title="Shell, I/O Redirection">Shell, I/O Redirection</a></li>
        <li><a href="https://intranet.hbtn.io/rltoken/6G_Cu3hczr_SdaSzlunjZg" target="_blank" title="Special Characters">Special Characters</a></li>
    </ul>
    <p><strong>man or help</strong>:</p>
    <ul>
        <li><code>echo</code></li>
        <li><code>cat</code></li>
        <li><code>head</code></li>
        <li><code>tail</code></li>
        <li><code>find</code></li>
        <li><code>wc</code></li>
        <li><code>sort</code></li>
        <li><code>uniq</code></li>
        <li><code>grep</code></li>
        <li><code>tr</code></li>
        <li><code>rev</code></li>
        <li><code>cut</code></li>
        <li><code>passwd (5)</code> (<em>i.e.&nbsp;<code>man 5 passwd</code></em>)</li>
    </ul>
    <h2>Learning Objectives</h2>
    <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/35eszk_xq3C3s4TzIrb-ng" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
    <h3>Shell, I/O Redirection</h3>
    <ul>
        <li>What do the commands&nbsp;<code>head</code>,&nbsp;<code>tail</code>,&nbsp;<code>find</code>,&nbsp;<code>wc</code>,&nbsp;<code>sort</code>,&nbsp;<code>uniq</code>,&nbsp;<code>grep</code>,&nbsp;<code>tr</code> do</li>
        <li>How to redirect standard output to a file</li>
        <li>How to get standard input from a file instead of the keyboard</li>
        <li>How to send the output from one program to the input of another program</li>
        <li>How to combine commands and filters with redirections</li>
    </ul>
    <h3>Special Characters</h3>
    <ul>
        <li>What are special characters</li>
        <li>Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them</li>
    </ul>
    <h3>Other Man Pages</h3>
    <ul>
        <li>How to display a line of text</li>
        <li>How to concatenate files and print on the standard output</li>
        <li>How to reverse a string</li>
        <li>How to remove sections from each line of files</li>
        <li>What is the&nbsp;<code>/etc/passwd</code> file and what is its format</li>
        <li>What is the&nbsp;<code>/etc/shadow</code> file and what is its format</li>
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
        <li>You are not allowed to use backticks,&nbsp;<code>&amp;&amp;</code>,&nbsp;<code>||</code> or&nbsp;<code>;</code></li>
        <li>All your files must be executable</li>
        <li>You are not allowed to use&nbsp;<code>sed</code> or&nbsp;<code>awk</code></li>
    </ul>
    <h2>More Info</h2>
    <p>Read your&nbsp;<code>/etc/passwd</code> and&nbsp;<code>/etc/shadow</code> files.</p>
    <p>Note: You do not have to learn about&nbsp;<code>fmt</code>,&nbsp;<code>pr</code>,&nbsp;<code>du</code>,&nbsp;<code>gzip</code>,&nbsp;<code>tar</code>,&nbsp;<code>lpr</code>,&nbsp;<code>sed</code> and&nbsp;<code>awk</code> yet.</p>
</div>
<br>
<h1>Tasks</h1>
<h2>0. Hello World</h2>
<p>Write a script that prints &ldquo;Hello, World&rdquo;, followed by a new line to the standard output.</p>
<p><b><i><u>The output should be:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/h$ ./0-hello_world 
Hello, World
julien@ubuntu:/tmp/h$ ./0-hello_world | cat -e
Hello, World$
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/0-hello_world" target="_blank">0-hello_world</b></i></a></code></li>
</ul>
<br>
<h2>1. Confused smiley</h2>
<p>Write a script that displays a confused smiley&nbsp;<code>&quot;(&Ocirc;o)&apos;</code>.&nbsp;</p>
<p><b><i><u>The output should be:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/h$ ./1-confused_smiley 
&quot;(&Ocirc;o)&apos;
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/1-confused_smiley" target="_blank">1-confused_smiley</b></i></a></code></li>
</ul>
<br>
<h2>2. Let's display a file</h2>
<p>Display the content of the&nbsp;<code>/etc/passwd</code> file.</p>
<p>Example:</p>
<pre><code>$ ./2-hellofile
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false
_ces:*:32:32:Certificate Enrollment Service:/var/empty:/usr/bin/false
_mcxalr:*:54:54:MCX AppLaunch:/var/empty:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/2-hellofile" target="_blank">2-hellofile</b></i></a></code></li>
</ul>
<br>
<h2>3. What about 2?</h2>
<p>Display the content of&nbsp;<code>/etc/passwd</code> and&nbsp;<code>/etc/hosts</code></p>
<p>Example:</p>
<pre><code>$ ./3-twofiles
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting. Do not change this entry.
##
127.0.0.1   localhost
255.255.255.255 broadcasthost
::1 localhost
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/3-twofiles" target="_blank">3-twofiles</b></i></a></code></li>
</ul>
<br>
<h2>4. Last lines of a file</h2>
<p>Display the last 10 lines of&nbsp;<code>/etc/passwd</code></p>
<p>Example:</p>
<pre><code>$ ./4-lastlines
_assetcache:*:235:235:Asset Cache Service:/var/empty:/usr/bin/false
_coremediaiod:*:236:236:Core Media IO Daemon:/var/empty:/usr/bin/false
_launchservicesd:*:239:239:_launchservicesd:/var/empty:/usr/bin/false
_iconservices:*:240:240:IconServices:/var/empty:/usr/bin/false
_distnote:*:241:241:DistNote:/var/empty:/usr/bin/false
_nsurlsessiond:*:242:242:NSURLSession Daemon:/var/db/nsurlsessiond:/usr/bin/false
_nsurlstoraged:*:243:243:NSURLStorage Daemon:/var/empty:/usr/bin/false
_displaypolicyd:*:244:244:Display Policy Daemon:/var/empty:/usr/bin/false
_astris:*:245:245:Astris Services:/var/db/astris:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
</code></pre>
<p><b>Tip: </b>“Thinks of it as a cat, what is at the end of it?”</p>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/4-lastlines" target="_blank">4-lastlines</b></i></a></code></li>
</ul>
<br>
<h2>5. I'd prefer the first ones actually</h2>
<p>Display the first 10 lines of&nbsp;<code>/etc/passwd</code></p>
<p>Example:</p>
<pre></code>$ ./5-firstlines
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
$
</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/5-firstlines" target="_blank">5-firstlines</b></i></a></code></li>
</ul>
<br>
<h2>6. Line #2</h2>
<p>Write a script that displays the third line of the file&nbsp;<code>iacta</code>.</p>
<p>The file&nbsp;<code>iacta</code> will be in the working directory</p>
<ul>
    <li>You&rsquo;re not allowed to use&nbsp;<code>sed</code></li>
</ul>
<p>Example:</p>
<pre><code>julien@ubuntu:/tmp/h$ cat iacta 
Alea iacta est

Alea iacta est (&quot;The die is cast&quot;) is a Latin phrase attributed by Suetonius
(as iacta alea est) to Julius Caesar on January 10, 49 BC
as he led his army across the Rubicon river in Northern Italy. With this step,
he entered Italy at the head of his army in defiance of the Senate and began
his long civil war against Pompey and the Optimates. The phrase has been
adopted in Italian (Il dado &egrave; tratto), Romanian (Zarurile au fost aruncate),
Spanish (La suerte est&aacute; echada), French (Les d&eacute;s sont jet&eacute;s), Portuguese (A
sorte est&aacute; lan&ccedil;ada), Dutch (De teerling is geworpen),
German (Der W&uuml;rfel ist gefallen), Hungarian (A kocka el van vetve) and many other languages to
indicate that events have passed a point of no return.

Read more: https://en.wikipedia.org/wiki/Alea_iacta_est
julien@ubuntu:/tmp/h$ ./6-third_line 
Alea iacta est (&quot;The die is cast&quot;) is a Latin phrase attributed by Suetonius
julien@ubuntu:/tmp/h$</code></pre>
<p><b>Note: </b>The output will differ, depending on the content of the file&nbsp;<code>iacta</code>.&nbsp;</p>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/6-third_line" target="_blank">6-third_line</b></i></a></code></li>
</ul>
<br>
<h2>7. It is a good file that cuts iron without making a noise</h2>
<p>Write a shell script that creates a file named exactly&nbsp;<code>\*\\&apos;&quot;Best School&quot;\&apos;\\*$\?\*\*\*\*\*:)</code> containing the text&nbsp;<code>Best School</code> ending by a new line.&nbsp;</p>
<pre><code>julien@ubuntu:~/shell$ ls &amp;&amp; ./7-file &amp;&amp; ls -l &amp;&amp; cat -e \\*
0-mac_and_cheese 7-file 7-file~ Makefile
total 20
-rwxrw-r-- 1 julien julien 79 Jan 20 06:24 0-mac_and_cheese
-rwxrw-r-- 1 julien julien 90 Jan 20 06:40 7-file
-rwxrw-r-- 1 julien julien 69 Jan 20 06:37 7-file~
-rw-rw-r-- 1 julien julien 14 Jan 20 06:38 Makefile
-rw-rw-r-- 1 julien julien 17 Jan 20 06:40 &apos;\*\\&apos;&quot;Best School&quot;\&apos;\\*$\?\*\*\*\*\*:)&apos;
Best School$
julien@ubuntu:~/shell$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/7-file" target="_blank">7-file</b></i></a></code></li>
</ul>
<br>
<h2>8. Save current state of directory</h2>
<p>Write a script that writes into the file&nbsp;<code>ls_cwd_content</code> the result of the command&nbsp;<code>ls -la</code>. If the file&nbsp;<code>ls_cwd_content</code> already exists, it should be overwritten. If the file&nbsp;<code>ls_cwd_content</code> does not exist, create it.&nbsp;</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/h$ ls -la
total 20
drwxrwxr-x  2 julien julien 4096 Sep 20 18:18 .
drwxrwxrwt 13 root   root   4096 Sep 20 18:18 ..
-rwxrw-r--  1 julien julien   36 Sep 20 18:18 8-cwd_state
-rw-rw-r--  1 betty  julien   23 Sep 20 14:25 hello
-rw-rw-r--  1 julien julien  926 Sep 20 17:52 iacta
julien@ubuntu:/tmp/h$ ./8-cwd_state 
julien@ubuntu:/tmp/h$ ls -la
total 24
drwxrwxr-x  2 julien julien 4096 Sep 20 18:18 .
drwxrwxrwt 13 root   root   4096 Sep 20 18:18 ..
-rwxrw-r--  1 julien julien   36 Sep 20 18:18 8-cwd_state
-rw-rw-r--  1 betty  julien   23 Sep 20 14:25 hello
-rw-rw-r--  1 julien julien  926 Sep 20 17:52 iacta
-rw-rw-r--  1 julien julien  329 Sep 20 18:18 ls_cwd_content
julien@ubuntu:/tmp/h$ cat ls_cwd_content 
total 20
drwxrwxr-x  2 julien julien 4096 Sep 20 18:18 .
drwxrwxrwt 13 root   root   4096 Sep 20 18:18 ..
-rwxrw-r--  1 julien julien   36 Sep 20 18:18 8-cwd_state
-rw-rw-r--  1 betty  julien   23 Sep 20 14:25 hello
-rw-rw-r--  1 julien julien  926 Sep 20 17:52 iacta
-rw-rw-r--  1 julien julien    0 Sep 20 18:18 ls_cwd_content
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/8-cwd_state" target="_blank">8-cwd_state</b></i></a></code></li>
</ul>
<br>
<h2>9. Duplicate last line</h2>
<p>Write a script that duplicates the last line of the file&nbsp;<code>iacta</code></p>
<ul>
    <li>The file&nbsp;<code>iacta</code> will be in the working directory</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/h$ cat iacta 
Alea iacta est

Alea iacta est (&quot;The die is cast&quot;) is a Latin phrase attributed by Suetonius
(as iacta alea est) to Julius Caesar on January 10, 49 BC
as he led his army across the Rubicon river in Northern Italy. With this step,
he entered Italy at the head of his army in defiance of the Senate and began
his long civil war against Pompey and the Optimates. The phrase has been
adopted in Italian (Il dado &egrave; tratto), Romanian (Zarurile au fost aruncate),
Spanish (La suerte est&aacute; echada), French (Les d&eacute;s sont jet&eacute;s), Portuguese (A
sorte est&aacute; lan&ccedil;ada), Dutch (De teerling is geworpen),
German (Der W&uuml;rfel ist gefallen), Hungarian (A kocka el van vetve) and many other languages to
indicate that events have passed a point of no return.

Read more: https://en.wikipedia.org/wiki/Alea_iacta_est
julien@ubuntu:/tmp/h$ ./9-duplicate_last_line 
julien@ubuntu:/tmp/h$ cat iacta 
Alea iacta est

Alea iacta est (&quot;The die is cast&quot;) is a Latin phrase attributed by Suetonius
(as iacta alea est) to Julius Caesar on January 10, 49 BC
as he led his army across the Rubicon river in Northern Italy. With this step,
he entered Italy at the head of his army in defiance of the Senate and began
his long civil war against Pompey and the Optimates. The phrase has been
adopted in Italian (Il dado &egrave; tratto), Romanian (Zarurile au fost aruncate),
Spanish (La suerte est&aacute; echada), French (Les d&eacute;s sont jet&eacute;s), Portuguese (A
sorte est&aacute; lan&ccedil;ada), Dutch (De teerling is geworpen),
German (Der W&uuml;rfel ist gefallen), Hungarian (A kocka el van vetve) and many other languages to
indicate that events have passed a point of no return.

Read more: https://en.wikipedia.org/wiki/Alea_iacta_est
Read more: https://en.wikipedia.org/wiki/Alea_iacta_est
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/9-duplicate_last_line" target="_blank">9-duplicate_last_line</b></i></a></code></li>
</ul>
<br>
<h2>10. No more javascript</h2>
<p>Write a script that deletes all the regular files (not the directories) with a&nbsp;<code>.js</code> extension that are present in the current directory and all its subfolders.&nbsp;</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/h$ ls -lR
.:
total 24
-rwxrw-r-- 1 julien julien   49 Sep 20 18:29 10-no_more_js
drwxrwxr-x 2 julien julien 4096 Sep 20 18:23 dir1
drwxrwxr-x 2 julien julien 4096 Sep 20 18:24 dir.js
-rw-rw-r-- 1 betty  julien   23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  982 Sep 20 18:21 iacta
-rw-rw-r-- 1 julien julien  329 Sep 20 18:18 ls_cwd_content
-rw-rw-r-- 1 julien julien    0 Sep 20 18:23 main.js

./dir1:
total 0
-rw-rw-r-- 1 julien julien 0 Sep 20 18:23 code.js

./dir.js:
total 0
julien@ubuntu:/tmp/h$ ./10-no_more_js 
julien@ubuntu:/tmp/h$ ls -lR
.:
total 24
-rwxrw-r-- 1 julien julien   49 Sep 20 18:29 10-no_more_js
drwxrwxr-x 2 julien julien 4096 Sep 20 18:29 dir1
drwxrwxr-x 2 julien julien 4096 Sep 20 18:24 dir.js
-rw-rw-r-- 1 betty  julien   23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  982 Sep 20 18:21 iacta
-rw-rw-r-- 1 julien julien  329 Sep 20 18:18 ls_cwd_content

./dir1:
total 0

./dir.js:
total 0
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/10-no_more_js" target="_blank">10-no_more_js</b></i></a></code></li>
</ul>
<br>
<h2>11. Don't just count your directories, make your directories count</h2>
<p>Write a script that counts the number of directories and sub-directories in the current directory.</p>
<ul>
    <li>The current and parent directories should not be taken into account</li>
    <li>Hidden directories should be counted</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@production-503e7013:~/shell/fun_with_the_shell$ ls -lRa
.:
total 32
drwxrwxr-x 3 julien julien 4096 Jan 20 03:53 .
drwxrwxr-x 3 julien julien 4096 Jan 20 02:58 ..
-rwxr--r-- 1 julien julien 43 Jan 20 02:59 0-commas
-rwxr--r-- 1 julien julien 47 Jan 20 02:50 1-empty_casks
-rwxrw-r-- 1 julien julien 68 Jan 20 03:35 2-gifs
-rwxrw-r-- 1 julien julien 47 Jan 20 03:53 3-directories
-rw-rw-r-- 1 julien julien 14 Jan 20 03:35 Makefile
drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 test_dir

./test_dir:
total 16
drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 .
drwxrwxr-x 3 julien julien 4096 Jan 20 03:53 ..
-rw-rw-r-- 1 julien julien 0 Jan 20 03:40 .horrible_selfie.gif
-rw-rw-r-- 1 julien julien 0 Jan 20 03:23 README.md
-rw-rw-r-- 1 julien julien 0 Jan 20 03:17 docker.gif
-rw-rw-r-- 1 julien julien 0 Jan 20 03:17 file.sh
drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 photos
drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 rep.gif

./test_dir/photos:
total 8
drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 .
drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 ..
-rw-rw-r-- 1 julien julien 0 Jan 20 03:23 cat.gif
-rw-rw-r-- 1 julien julien 0 Jan 20 03:22 index.html
-rw-rw-r-- 1 julien julien 0 Jan 20 03:23 main.gif
-rw-rw-r-- 1 julien julien 0 Jan 20 03:23 rudy_rigot.gif

./test_dir/rep.gif:
total 8
drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 .
drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 ..
julien@production-503e7013:~/shell/fun_with_the_shell$ ./11-directories
3
julien@production-503e7013:~/shell/fun_with_the_shell$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/11-directories" target="_blank">11-directories</b></i></a></code></li>
</ul>
<br>
<h2>12. What’s new</h2>
<p>Create a script that displays the 10 newest files in the current directory.</p>
<p>Requirements:</p>
<ul>
    <li>One file per line</li>
    <li>Sorted from the newest to the oldest</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>alex@ubuntu:/tmp$ ls -l
total 7
-rwxr-xr-x 1 501 dialout  32 Sep 27 23:51 0-hello_world
-rwxr-xr-x 1 501 dialout  46 Sep 28 11:09 10-no_more_js
-rwxr-xr-x 1 501 dialout  43 Sep 28 11:19 11-directories
-rwxr-xr-x 1 501 dialout  30 Sep 29 13:43 12-newest_files
-rwxr-xr-x 1 501 dialout  28 Sep 27 23:54 1-confused_smiley
-rwxr-xr-x 1 501 dialout  28 Sep 27 23:58 2-hellofile
-rwxr-xr-x 1 501 dialout  39 Sep 27 23:58 3-twofiles
-rwxr-xr-x 1 501 dialout  33 Sep 27 23:59 4-lastlines
-rwxr-xr-x 1 501 dialout  33 Sep 28 00:00 5-firstlines
-rwxr-xr-x 1 501 dialout  28 Sep 28 00:25 6-third_line
-rwxr-xr-x 1 501 dialout 110 Sep 28 00:34 7-file
-rwxr-xr-x 1 501 dialout  36 Sep 28 00:34 8-cwd_state
-rwxr-xr-x 1 501 dialout  35 Sep 28 00:35 9-duplicate_last_line
-rw-r--r-- 1 501 dialout  19 Sep 27 23:51 README.md
alex@ubuntu:/tmp$ ./12-newest_files 
12-newest_files
11-directories
10-no_more_js
9-duplicate_last_line
7-file
8-cwd_state
6-third_line
5-firstlines
4-lastlines
3-twofiles
alex@ubuntu:/tmp$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/12-newest_files" target="_blank">12-newest_files</b></i></a></code></li>
</ul>
<br>
<h2>13. Being unique is better than being perfect</h2>
<p>Create a script that takes a list of words as input and prints only words that appear exactly once.</p>
<ul>
    <li>Input format: One line, one word</li>
    <li>Output format: One line, one word</li>
    <li>Words should be sorted</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x02$ cat list 
C#
C
Javascript
Perl
PHP
PHP
ASP
R
Go
C#
C++
R
Perl
Javascript
Javascript
Python
Javascript
Javascript
Javascript
Java
Java
Python
Javascript
Javascript
Javascript
ASP
julien@ubuntu:/tmp/0x02$ cat list | ./13-unique 
C
C++
Go
julien@ubuntu:/tmp/0x02$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/13-unique" target="_blank">13-unique</b></i></a></code></li>
</ul>
<br>
<h2>14. It must be in that file</h2>
<p>Display lines containing the pattern “root” from the file <code>/etc/passwd</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>$ ./14-findthatword
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_cvmsroot:*:212:212:CVMS Root:/var/empty:/usr/bin/false
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/14-findthatword" target="_blank">14-findthatword</b></i></a></code></li>
</ul>
<br>
<h2>15. Count that word</h2>
<p>Display the number of lines that contain the pattern “bin” in the file <code>/etc/passwd</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>$ ./15-countthatword
81
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/15-countthatword" target="_blank">15-countthatword</b></i></a></code></li>
</ul>
<br>
<h2>16. What's next?</h2>
<p>Display lines containing the pattern “root” and 3 lines after them in the file <code>/etc/passwd.</code></p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>$ ./16-whatsnext
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
--
_cvmsroot:*:212:212:CVMS Root:/var/empty:/usr/bin/false
_usbmuxd:*:213:213:iPhone OS Device Helper:/var/db/lockdown:/usr/bin/false
_dovecot:*:214:6:Dovecot Administrator:/var/empty:/usr/bin/false
_dpaudio:*:215:215:DP Audio:/var/empty:/usr/bin/false
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/16-whatsnext" target="_blank">16-whatsnext</b></i></a></code></li>
</ul>
<br>
<h2>17. I hate bins</h2>
<p>Display all the lines in the file <code>/etc/passwd</code> that do not contain the pattern “bin”.</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>$ ./17-hidethisword
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/17-hidethisword" target="_blank">17-hidethisword</b></i></a></code></li>
</ul>
<br>
<h2>18. Letters only please</h2>
<p>Display all lines of the file <code>/etc/ssh/sshd_config</code> starting with a letter.</p>
<ul>
    <li>Include capital letters as well</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre></code>$ ./18-letteronly
SyslogFacility AUTHPRIV
AuthorizedKeysFile  .ssh/authorized_keys
UsePrivilegeSeparation sandbox # Default for new installations.
AcceptEnv LANG LC_*
Subsystem   sftp    /usr/libexec/sftp-server
$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/18-letteronly" target="_blank">18-letteronly</b></i></a></code></li>
</ul>
<br>
<h2>19. A to Z</h2>
<p>Replace all characters <code>A</code> and <code>c</code> from input to <code>Z</code> and <code>e</code> respectively.</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x02$ echo 'Replace all characters `A` and `c` from input to `Z` and `e`.' | ./19-AZ 
Replaee all eharaeters `Z` and `e` from input to `Z` and `e`.
julien@ubuntu:/tmp/0x02$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/19-AZ" target="_blank">19-AZ</b></i></a></code></li>
</ul>
<br>
<h2>20. Without C, you would live in hiago</h2>
<p>Create a script that removes all letters <code>c</code> and <code>C</code> from input.</p>
<pre><code>julien@ubuntu:/tmp/0x02$ echo Chicago | ./20-hiago 
hiago
julien@ubuntu:/tmp/0x02$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/20-hiago" target="_blank">20-hiago</b></i></a></code></li>
</ul>
<br>
<h2>21. esreveR</h2>
<p>Write a script that reverse its input.</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x02$ echo "Reverse" | ./21-reverse 
esreveR
julien@ubuntu:/tmp/0x02$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/21-reverse" target="_blank">21-reverse</b></i></a></code></li>
</ul>
<br>
<h2>22. DJ Cut Killer</h2>
<p>Write a script that displays all users and their home directories, sorted by users.</p>
<ul>
    <li>Based on the the <code>/etc/passwd</code> file</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x02$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
julien:x:1000:1000:Julien Barbier,,,:/home/julien:/bin/bash
guillaume:x:1001:1001:,,,:/home/guillaume:/bin/bash
betty:x:1002:1002::/home/betty:
julien@ubuntu:/tmp/0x02$
julien@ubuntu:/tmp/0x02$ ./22-users_and_homes 
_apt:/nonexistent
avahi-autoipd:/var/lib/avahi-autoipd
avahi:/var/run/avahi-daemon
backup:/var/backups
betty:/home/betty
bin:/bin
colord:/var/lib/colord
daemon:/usr/sbin
dnsmasq:/var/lib/misc
games:/usr/games
gnats:/var/lib/gnats
guillaume:/home/guillaume
hplip:/var/run/hplip
irc:/var/run/ircd
julien:/home/julien
kernoops:/
lightdm:/var/lib/lightdm
list:/var/list
lp:/var/spool/lpd
mail:/var/mail
man:/var/cache/man
messagebus:/var/run/dbus
news:/var/spool/news
nobody:/nonexistent
proxy:/bin
pulse:/var/run/pulse
root:/root
rtkit:/proc
saned:/var/lib/saned
speech-dispatcher:/var/run/speech-dispatcher
sync:/bin
sys:/dev
syslog:/home/syslog
systemd-bus-proxy:/run/systemd
systemd-network:/run/systemd/netif
systemd-resolve:/run/systemd/resolve
systemd-timesync:/run/systemd
usbmux:/var/lib/usbmux
uucp:/var/spool/uucp
uuidd:/run/uuidd
whoopsie:/nonexistent
www-data:/var/www
julien@ubuntu:/tmp/0x02$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/22-users_and_homes" target="_blank">22-users_and_homes</b></i></a></code></li>
</ul>
<br>
<h2>23. Empty casks make the most noise</h2>
<p><b><i>Advanced task</i></b><p>
<p>Write a command that finds all empty files and directories in the current directory and all sub-directories.</p>
<ul>
    <li>Only the names of the files and directories should be displayed (not the entire path)</li>
    <li>Hidden files should be listed</li>
    <li>One file name per line</li>
    <li>The listing should end with a new line</li>
    <li>You are not allowed to use <code>basename</code>, <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$ ls -laR
.:
total 64
drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 .
drwxrwxr-x 7 ubuntu ubuntu 4096 Sep 29 21:36 ..
-rwxrwxr-x 1 ubuntu ubuntu   56 Feb  8  2016 0-commas
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 0-commas-checks
-rwxrwxr-x 1 ubuntu ubuntu   48 Feb  8  2016 1-empty_casks
-rwxrwxr-x 1 ubuntu ubuntu   68 Feb  8  2016 2-gifs
-rwxrwxr-x 1 ubuntu ubuntu   47 Feb  8  2016 3-directories
-rwxrwxr-x 1 ubuntu ubuntu   41 Feb  8  2016 4-zeros
-rwxrwxr-x 1 ubuntu ubuntu   43 Feb  8  2016 5-rot13
-rwxrwxr-x 1 ubuntu ubuntu   25 Feb  8  2016 6-odd
-rwxrwxr-x 1 ubuntu ubuntu   73 Feb  8  2016 7-sort_rot13
-rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:46 ........gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:47 ..hello.gif
drwxrwxr-x 2 ubuntu ubuntu 4096 Oct  7 00:41 javascript
-rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:48 Kris_is_awesome :)
-rw-rw-r-- 1 ubuntu ubuntu   14 Feb  8  2016 Makefile
-rw-rw-r-- 1 ubuntu ubuntu   69 Feb  8  2016 quote
-rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:24 Rona_napping.gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Oct  6 23:59 root.gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Mar 24  2016 ..something
drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 test_dir
-rwxrwxr-x 1 ubuntu ubuntu   54 Feb  8  2016 test.var

./0-commas-checks:
total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 .
drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..
-rw-rw-r-- 1 ubuntu ubuntu 1361 Feb  8  2016 28-check.php
-rw-rw-r-- 1 ubuntu ubuntu  481 Feb  8  2016 28-check.php~

./javascript:
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Oct  7 00:41 .
drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..

./test_dir:
total 12
drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 .
drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 docker.gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 file.sh
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 .horrible_selfie.gif
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 photos
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 README.md

./test_dir/photos:
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 cat.gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 index.html
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 main.gif
-rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 rudy_rigot.gif
ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$ ./100-empty_casks
Rona_napping.gif
javascript
root.gif
..something
Kris_is_awesome :)
..hello.gif
file.sh
docker.gif
README.md
index.html
main.gif
cat.gif
rudy_rigot.gif
.horrible_selfie.gif
........gif
ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x02-shell_redirections/100-empty_casks" target="_blank">100-empty_casks</b></i></a></code></li>
</ul>
