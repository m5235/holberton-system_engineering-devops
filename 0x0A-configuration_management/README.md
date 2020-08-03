Puppet Mode
_________________________________________________________________________
License GPL 3 travis

Puppet Mode lets you edit Puppet 3 manifests with GNU Emacs 24.

Puppet Mode is a major mode for GNU Emacs 24 which adds support for the Puppet language. Puppet is a system provisioning and configuration tool by Puppetlabs Inc. This mode supports Puppet 3 and later. Puppet 2 is not explicitly supported anymore, but should mostly work.

This mode needs GNU Emacs 24. It will not work with GNU Emacs 23 and below, or with other flavors of Emacs (e.g. XEmacs).

Features
 1. Syntax highlighting
 2. Indentation and alignment of expressions and statements
 3. Tag navigation (aka imenu)
 4. Manual validation and linting of manifests (see Flycheck for on-the-fly validation and linting)
Integration with Puppet Debugger

Installation
_________________________________________________________________________

From MELPA or MELPA Stable with M-x package-install RET puppet-mode. Users of Debian ≥11 and derivatives can sudo apt install elpa-puppet-mode. Manifest validation and linting support is enabled by installing the elpa-flycheck package.

In your Cask file:

(source melpa)

(depends-on "puppet-mode")
Usage
Just visit Puppet manifests. The major mode is enabled automatically for Puppet manifests with the extension .pp.

The following key bindings are available in Puppet Mode:

Key	Command
C-M-a	Move to the beginning of the current block
C-M-e	Move to the end of the current block
C-c C-a	Align parameters in the current block
C-c C-'	Toggle string quoting between single and double
C-c C-;	Blank the string at point
C-c C-j	Jump to a class, define, variable or resource
C-c C-c	Apply the current manifest in dry-run mode
C-c C-v	Validate the syntax of the current manifest
C-c C-l	Check the current manifest for semantic issues
C-c C-z	Launch a puppet-debugger REPL
C-c C-r	Send the currently marked region to the REPL
C-c C-b	Send the current buffer to the REPL
For the integration with puppet-debugger to work, the puppet-debugger gem needs to be installed and available in your $PATH. See the instructions on puppet-debugger's repository on how to install it.

Use M-x customize-group RET puppet to customize Puppet Mode.

Support
Feel free to ask question or make suggestions in our issue tracker.

Contribute
Issue tracker
Github
License
Puppet Mode is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Puppet Mode is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

See COPYING for the complete license.