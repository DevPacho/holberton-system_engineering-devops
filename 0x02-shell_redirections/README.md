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
