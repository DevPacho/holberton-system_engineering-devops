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
<p>Create a script that creates an alias.</p>
<ul>
    <li>Name: <code>ls</code></li>
    <li>Value: <code>rm *</code></li>
</ul>
    <p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x03$ ls
0-alias  file1  file2
julien@ubuntu:/tmp/0x03$ source ./0-alias 
julien@ubuntu:/tmp/0x03$ ls
julien@ubuntu:/tmp/0x03$ \ls
julien@ubuntu:/tmp/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/0-alias" target="_blank">0-alias</b></i></a></code></li>
</ul>
<br>
<h2>1. Hello you</h2>
    <p>Create a script that prints <code>hello user</code>, where user is the current Linux user.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@ubuntu:/tmp/0x03$ id
uid=1000(julien) gid=1000(julien) groups=1000(julien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
julien@ubuntu:/tmp/0x03$ ./1-hello_you 
hello julien
julien@ubuntu:/tmp/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/1-hello_you" target="_blank">1-hello_you</b></i></a></code></li>
</ul>
    <br>
    <h2>2. The path to success is to take massive, determined action</h2>
    <p>Add <code>/action</code> to the <code>PATH</code>. <code>/action</code> should be the last directory the shell looks into when looking for a program.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ source ./2-path 
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/action
julien@ubuntu:/tmp/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/2-path" target="_blank">2-path</b></i></a></code></li>
</ul>
    <br>
    <h2>3. If the path be beautiful, let us not ask where it leads</h2>
    <p>Create a script that counts the number of directories in the <code>PATH</code>.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ . ./3-paths 
11
julien@ubuntu:/tmp/0x03$ PATH=/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:::::/hello
julien@ubuntu:/tmp/0x03$ . ./3-paths 
12
julien@ubuntu:/tmp/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/3-paths" target="_blank">3-paths</b></i></a></code></li>
</ul>
    <br>
    <h2>4. Global variables</h2>
    <p>Create a script that lists environment variables.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@ubuntu:/tmp/0x03$ source ./4-global_variables
CC=gcc
CDPATH=.:~:/usr/local:/usr:/
CFLAGS=-O2 -fomit-frame-pointer
COLORTERM=gnome-terminal
CXXFLAGS=-O2 -fomit-frame-pointer
DISPLAY=:0
DOMAIN=hq.garrels.be
e=
TOR=vi
FCEDIT=vi
FIGNORE=.o:~
G_BROKEN_FILENAMES=1
GDK_USE_XFT=1
GDMSESSION=Default
GNOME_DESKTOP_SESSION_ID=Default
GTK_RC_FILES=/etc/gtk/gtkrc:/nethome/franky/.gtkrc-1.2-gnome2
GWMCOLOR=darkgreen
GWMTERM=xterm
HISTFILESIZE=5000
history_control=ignoredups
HISTSIZE=2000
HOME=/nethome/franky
HOSTNAME=octarine.hq.garrels.be
INPUTRC=/etc/inputrc
IRCNAME=franky
JAVA_HOME=/usr/java/j2sdk1.4.0
LANG=en_US
LDFLAGS=-s
LD_LIBRARY_PATH=/usr/lib/mozilla:/usr/lib/mozilla/plugins
LESSCHARSET=latin1
LESS=-edfMQ
LESSOPEN=|/usr/bin/lesspipe.sh %s
LEX=flex
LOCAL_MACHINE=octarine
LOGNAME=franky
[...]
julien@ubuntu:/tmp/0x03$</code></pre>
    <ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/4-global_variables" target="_blank">4-global_variables</b></i></a></code></li>
</ul>
    <br>
    <h2>5. Local variables</h2>
    <p>Create a script that lists all local variables and environment variables, and functions.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@ubuntu:/tmp/0x03$ . ./5-local_variables
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:histappend:interactive_comments:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
BASH_LINENO=()
BASH_REMATCH=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="4" [1]="3" [2]="46" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='4.3.46(1)-release'
CLUTTER_IM_MODULE=xim
COLUMNS=133
COMPIZ_CONFIG_PROFILE=ubuntu
COMP_WORDBREAKS=$' \t\n"\'><=;|&(:'
DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-Fg27Lr20bq
DEFAULTS_PATH=/usr/share/gconf/ubuntu.default.path
DESKTOP_SESSION=ubuntu
[...]
julien@ubuntu:/tmp/0x03$</code></pre>
    <ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/5-local_variables" target="_blank">5-local_variables</b></i></a></code></li>
</ul>
    <br>
    <h2>6. Local variable</h2>
    <p>Create a script that creates a new local variable.</p>
<ul>
    <li>Name: <code>BEST</code></li>
    <li>Value: <code>SCHOOL</code></li>
</ul>
    <ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/6-create_local_variable" target="_blank">6-create_local_variable</b></i></a></code></li>
</ul>
<br>
    <h2>7. Global variable</h2>
    <p>Create a script that creates a new global variable.</p>
<ul>
    <li>Name: <code>BEST</code></li>
    <li>Value: <code>SCHOOL</code></li>
</ul>
    <ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/7-create_global_variable" target="_blank">7-create_global_variable</b></i></a></code></li>
</ul>
<br>
    <h2>8. Every addition to true knowledge is an addition to human power</h2>
    <p>Write a script that prints the result of the addition of 128 with the value stored in the environment variable <code>TRUEKNOWLEDGE</code>, followed by a new line.</p>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@production-503e7013:~$ export TRUEKNOWLEDGE=1209
julien@production-503e7013:~$ ./8-true_knowledge | cat -e
1337$
julien@production-503e7013:~$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/8-true_knowledge" target="_blank">8-true_knowledge</b></i></a></code></li>
</ul>
    <br>
    <h2>9. Divide and rule</h2>
    <p>Write a script that prints the result of&nbsp;<code>POWER</code> divided by&nbsp;<code>DIVIDE</code>, followed by a new line.</p>
<ul>
    <li><code>POWER</code> and&nbsp;<code>DIVIDE</code> are environment variables</li>
</ul>
    <p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@production-503e7013:~$ export POWER=42784
julien@production-503e7013:~$ export DIVIDE=32
julien@production-503e7013:~$ ./9-divide_and_rule | cat -e
1337$
julien@production-503e7013:~$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/9-divide_and_rule" target="_blank">9-divide_and_rule</b></i></a></code></li>
</ul>
    <br>
    <h2>10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath</h2>
    <p>Write a script that displays the result of&nbsp;<code>BREATH</code> to the power&nbsp;<code>LOVE</code></p>
<ul>
    <li><code>BREATH</code> and&nbsp;<code>LOVE</code> are environment variables</li>
    <li>The script should display the result, followed by a new line</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
    <pre><code>julien@production-503e7013:~/$ export BREATH=4
julien@production-503e7013:~/$ export LOVE=3
julien@production-503e7013:~/$ ./10-love_exponent_breath
64
julien@production-503e7013:~/$</code></pre>
    <ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/10-love_exponent_breath" target="_blank">10-love_exponent_breath</b></i></a></code></li>
</ul>
    <br>
    <h2>11. There are 10 types of people in the world -- Those who understand binary, and those who don't</h2>
    <p>Write a script that converts a number from base 2 to base 10.</p>
<ul>
    <li>The number in base 2 is stored in the environment variable&nbsp;<code>BINARY</code></li>
    <li>The script should display the number in base 10, followed by a new line</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@production-503e7013:~/$ export BINARY=10100111001
julien@production-503e7013:~/$ ./11-binary_to_decimal
1337
julien@production-503e7013:~/$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/11-binary_to_decimal" target="_blank">11-binary_to_decimal</b></i></a></code></li>
</ul>
<br>
<h2>12. Combination</h2>
<p>Create a script that prints all possible combinations of two letters, except&nbsp;<code>oo</code>.</p>
<ul>
    <li>Letters are lower cases, from&nbsp;<code>a</code> to&nbsp;<code>z</code></li>
    <li>One combination per line</li>
    <li>The output should be alpha ordered, starting with&nbsp;<code>aa</code></li>
    <li>Do not print&nbsp;<code>oo</code></li>
    <li>Your script file should contain maximum 64 characters</li>
</ul>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>julien@ubuntu:/tmp/0x03$ echo $((26 ** 2 -1))
675
julien@ubuntu:/tmp/0x03$ ./12-combinations | wc -l
675
julien@ubuntu:/tmp/0x03$ 
julien@ubuntu:/tmp/0x03$ ./12-combinations | tail -303 | head -10
oi
oj
ok
ol
om
on
op
oq
or
os
julien@ubuntu:/tmp/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/12-combinations" target="_blank">12-combinations</b></i></a></code></li>
</ul>
<br>
<h2>13. Floats</h2>
<p>Write a script that prints a number with two decimal places, followed by a new line.</p>
<p>The number will be stored in the environment variable&nbsp;<code>NUM</code>.</p>
<p><b><i><u>Output example:</u></i></b></p>
<pre><code>ubuntu@ip-172-31-63-244:~/0x03$ export NUM=0
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
0.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=98
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
98.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=3.14159265359
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
3.14
ubuntu@ip-172-31-63-244:~/0x03$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/13-print_float" target="_blank">13-print_float</b></i></a></code></li>
</ul>
<br>
<h2>14. Decimal to Hexadecimal</h2>
<p><b><i>Advanced task</i></b><p>
<p>Write a script that converts a number from base 10 to base 16.</p>
<ul>
    <li>The number in base 10 is stored in the environment variable&nbsp;<code>DECIMAL</code></li>
    <li>The script should display the number in base 16, followed by a new line</li>
</ul>
<pre><code>julien@production-503e7013:~/$ export DECIMAL=16
julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal
10
julien@production-503e7013:~/$ export DECIMAL=1337
julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal | cat -e
539$
julien@production-503e7013:~/$ export DECIMAL=15
julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal | cat -e
f$
julien@production-503e7013:~/$</code></pre>
<ul>
    <li><b>File:</b>&nbsp;<code><i><b><a href="https://github.com/FranRM15/holberton-system_engineering-devops/blob/main/0x03-shell_variables_expansions/100-decimal_to_hexadecimal" target="_blank">100-decimal_to_hexadecimal</b></i></a></code></li>
</ul>
<br>
<h2>15. What is the difference between a hard link and a symbolic link?</h2>
<p><b><i>Advanced task</i></b><p>
<p>Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two. Use examples to illustrate.</p>
<ul>
    <li>Have at least one picture, at the top of the blog post</li>
    <li>Publish your blog post on Medium or LinkedIn</li>
    <li>Share your blog post at least on LinkedIn</li>
</ul>
<ul>
    <li><b>You can read my blog giving an answer to the previous problematizing question</b>&nbsp;<code><i><b><a href="https://www.linkedin.com/pulse/hard-symbolic-links-francisco-jos%25C3%25A9-ram%25C3%25ADrez-mojica" target="_blank">HERE ON MY LINKEDIN!</b></i></a></code></li>
</ul>
