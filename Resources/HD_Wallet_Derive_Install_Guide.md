# HD-Wallet-Derive Install Guide

This guide serves as a step by step process for setting up the [`hd-wallet-derive` library](https://github.com/dan-da/hd-wallet-derive) used to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins or "altcoins."

If you need additional help in the installation process, you can follow the step by step video guides in the following links.
* [Installing PHP Using the Homebrew Package Manger for Mac](https://youtu.be/SNRQSwlOKbs)

* [HD Derive Wallet Install for Mac](https://youtu.be/c-Qc3Pss6oM)


## For those using **macOS**, execute the following steps:

# Step 1 - PHP installation

1. macOS users will need to update their machine's prebuilt version of PHP to the full version using a package manager for macOS called Homebrew.

2. To do this, visit the [Homebrew website](https://brew.sh/) and install Homebrew using the given install command.

3. Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.4 at this current time).

    brew update
    brew install php@7.4
    brew link --force --overwrite php@7.4
    brew services start php@7.4
    
4. Next, execute the command appropriate for your system:

    * macOS Catalina and above including Apple Silicon M1 (`zsh` shell):

      echo "export PATH=/usr/local/opt/php@7.4/bin:$PATH" >> ~/.zshrc

    * Versions prior to macOS Catalina (`bash` shell):

      echo "export PATH=/usr/local/opt/php@7.4/bin:$PATH" >> ~/.bash_profile


    * **Note:** If you are on macOS Catalina and up (10.15+), your default shell is now `zsh`, instead of `bash` as in previous versions. No worries, however, since `zsh` can handle the same tasks. If you have yet to upgrade to Catalina, you will be using `bash` as your default shell, which will affect the commands you need to run. Make sure you are running the commands appr
    
**Close the terminal**. 

5. Open a **NEW** terminal, then verify that PHP version 7.4 is the current version in your system by executing the following command:

    php -version
    
    
# Step 2 - Installing hd-wallet-derive 

With the latest version of PHP installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.


1. Begin by opening a fresh terminal.


2. With your terminal open, cd into your `Blockchain-Tools folder and run the following code:

      git clone https://github.com/dan-da/hd-wallet-derive
      cd hd-wallet-derive
      curl https://getcomposer.org/installer -o installer.php
      php installer.php
      php composer.phar install
    
    
3. You should now have a folder called `hd-wallet-derive` containing the PHP library!

# Confirm installation
 
1. Run the command to `cd` in your `hd-wallet-derive` folder.

2. Once you've confirmed your are in your `hd-wallet-derive` folder, execute the following command:

    ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change
