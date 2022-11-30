# Web stack debugging #3

Puppet manifests are interpreted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [Puppet v3.4.x](https://puppet.com/) and are [puppet-lint](http://puppet-lint.com/) compliant.

### Focus
Learn how to debug a webstack with `strace`.

### Example Usages

[0-strace_is_your_friend.pp](0-strace_is_your_friend.pp)
```
root@63ca2686979b:~# puppet apply 0-strace_is_your_friend.pp
```

### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
