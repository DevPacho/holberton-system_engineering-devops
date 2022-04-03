<h1>0x01. Shell, permissions</h1>
<img src="https://linuxcommand.org/images/file_permissions.png">
<div>
    <h2>About&nbsp;Bash&nbsp;projects</h2>
    <p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
</div>
<div>
    <h2>Resources</h2>
    <p><strong>Read or watch</strong>:</p>
    <ul>
        <li><a href="https://intranet.hbtn.io/rltoken/5uUsOHrMbVBOpZFteNyBLg" target="_blank" title="Permissions">Permissions</a></li>
    </ul>
    <p><strong>man or help</strong>:</p>
    <ul>
        <li><code>chmod</code></li>
        <li><code>sudo</code></li>
        <li><code>su</code></li>
        <li><code>chown</code></li>
        <li><code>chgrp</code></li>
        <li><code>id</code></li>
        <li><code>groups</code></li>
        <li><code>whoami</code></li>
        <li><code>adduser</code></li>
        <li><code>useradd</code></li>
        <li><code>addgroup</code></li>
    </ul>
    <h2>Learning Objectives</h2>
    <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/Y35d0Jims8dedreTJJiaAw" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
    <h3>Permissions</h3>
    <ul>
        <li>What do the commands&nbsp;<code>chmod</code>,&nbsp;<code>sudo</code>,&nbsp;<code>su</code>,&nbsp;<code>chown</code>,&nbsp;<code>chgrp</code> do</li>
        <li>Linux file permissions</li>
        <li>How to represent each of the three sets of permissions (owner, group, and other) as a single digit</li>
        <li>How to change permissions, owner and group of a file</li>
        <li>Why can&rsquo;t a normal user&nbsp;<code>chown</code> a file</li>
        <li>How to run a command with root privileges</li>
        <li>How to change user ID or become superuser</li>
    </ul>
    <h3>Other Man Pages</h3>
    <ul>
        <li>How to create a user</li>
        <li>How to create a group</li>
        <li>How to print real and effective user and group IDs</li>
        <li>How to print the groups a user is in</li>
        <li>How to print the effective userid</li>
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
    </ul>
</div>
<br>
<h1>Tasks</h1>
<h2>0. My name is Betty</h2>
<p>Create a script that switches the current user to the user&nbsp;<code>betty</code>.</p>
<ul>
    <li>You should use exactly 8 characters for your command (+1 character for the new line)</li>
    <li>You can assume that the user&nbsp;<code>betty</code> will exist when we will run your script</li>
</ul>
<pre><code>julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>0-iam_betty</code></li>
</ul>
<br>
<h2>1. Who am I</h2>
<p>Write a script that prints the effective username of the current user.</p>
<pre><code>julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$ </code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>1-who_am_i</code></li>
</ul>
<br>
<h2>2. Groups</h2>
<p>Write a script that prints all the groups the current user is part of.</p>
<pre><code>julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$ 
</code></pre>
<p>Note: depending on the user, you will get a different output.</p>
<ul>
    <li><b>File:</b>&nbsp;<code>2-groups</code></li>
</ul>
<br>
<h2>3. New owner</h2>
<p>Write a script that changes the owner of the file&nbsp;<code>hello</code> to the user&nbsp;<code>betty</code>.</p>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner 
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>3-new_owner</code></li>
</ul>
<br>
<h2>4. Empty!</h2>
<p>Write a script that creates an empty file called&nbsp;<code>hello</code>.&nbsp;</p>
<ul>
    <li><b>File:</b>&nbsp;<code>4-empty</code></li>
</ul>
<br>
<h2>5. Execute</h2>
<p>Write a script that adds execute permission to the owner of the file&nbsp;<code>hello</code>.</p>
<ul>
    <li>The file&nbsp;<code>hello</code> will be in the working directory</li>
</ul>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>5-execute</code></li>
</ul>
<br>
<h2>6. Multiple permissions</h2>
<p>Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file&nbsp;<code>hello</code>.</p>
<ul>
    <li>The file&nbsp;<code>hello</code> will be in the working directory</li>
</ul>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>6-multiple_permissions</code></li>
</ul>
<br>
<h2>7. Everybody!</h2>
<p>Write a script that adds execution permission to the owner, the group owner and the other users, to the file&nbsp;<code>hello</code></p>
<ul>
    <li>The file&nbsp;<code>hello</code> will be in the working directory</li>
    <li>You are not allowed to use commas for this script</li>
</ul>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ </code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>7-everybody</code></li>
</ul>
<br>
<h2>8. James Bond</h2>
<p>Write a script that sets the permission to the file&nbsp;<code>hello</code> as follows:</p>
<ul>
    <li>Owner: no permission at all</li>
    <li>Group: no permission at all</li>
    <li>Other users: all the permissions</li>
</ul>
<p>The file&nbsp;<code>hello</code> will be in the working directory You are not allowed to use commas for this script</p>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>8-James_Bond</code></li>
</ul>
<br>
<h2>9. John Doe</h2>
<p>Write a script that sets the mode of the file&nbsp;<code>hello</code> to this:</p>
<pre><code>-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
</code></pre>
<ul>
    <li>The file&nbsp;<code>hello</code> will be in the working directory</li>
    <li>You are not allowed to use commas for this script</li>
</ul>
<ul>
    <li><b>File:</b>&nbsp;<code>9-John_Doe</code></li>
</ul>
<br>
<h2>10. Look in the mirror</h2>
<p>Write a script that sets the mode of the file&nbsp;<code>hello</code> the same as&nbsp;<code>olleh</code>&rsquo;s mode.</p>
<ul>
    <li>The file&nbsp;<code>hello</code> will be in the working directory</li>
    <li>The file&nbsp;<code>olleh</code> will be in the working directory</li>
</ul>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ 
</code></pre>
<p>Note: the mode of&nbsp;<code>olleh</code> will not always be 664. Make sure your script works for any mode.</p>
<ul>
    <li><b>File:</b>&nbsp;<code>10-mirror_permissions</code></li>
</ul>
<br>
<h2>11. Directories</h2>
<p>Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.</p>
<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code>11-directories_permissions</code></li>
</ul>
<br>
<h2>12. More directories</h2>
