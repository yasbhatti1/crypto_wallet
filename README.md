# Multi-Blockchain Wallet in Python

## Background

Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there. It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.

You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, `hd-wallet-derive` that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.

Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.

In this assignment, however, I will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.


## Dependencies

The following dependencies are required for this project. 

> **Important:** If you have _not_ already installed the dependencies listed below, you may do so by following the instructions found in the following guides:
  > - [HD Wallet Derive Installation Guide](Resources/HD_Wallet_Derive_Install_Guide.md) 
  > - [Blockchain TX Installation Guide](Resources/Blockchain_TX_Install_Guide.md).

**Dependencies List:**
- PHP must be installed on your operating system.

- You will need to clone the [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) tool.

- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library.

- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library.


# Instructions

## Project Setup

Create a project directory called `wallet` and `cd` into it.

- Clone the `hd-wallet-derive` tool into this folder and install it using the [HD Wallet Derive Installation Guide](Resources/HD_Wallet_Derive_Install_Guide.md)

- Create a symlink called `derive` for the `hd-wallet-derive/hd-wallet-derive.php` script. This will clean up the command needed to run the script in our code, as we can call `./derive` instead of `./hd-wallet-derive/hd-wallet-derive.php`: 

  - Make sure you are in the top level project directory - in this case the directory named `wallet`. 
  
  - **Mac Users:** Run the following command: `ln -s hd-wallet-derive/hd-wallet-derive.php derive`. 

- Test that you can run the `./derive` script properly, by running the following command.  

      ./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g

 - The output should match what you see below:

      +------+-------------------------------------+
      | path | address                             |
      +------+-------------------------------------+
      | m/0  | t1V1Qp41kbHn159hvVXZL5M1MmVDRe6EdpA |
      | m/1  | t1Tw6iqFY1g9dKeAqPDAncaUjha8cn9SZqX |
      | m/2  | t1VGTPzBSSYd27GF8p9rGKGdFuWekKRhug4 |
      +------+-------------------------------------+

- Create a file called `wallet.py` -- this will be your universal wallet script.

Initial setup should look something like this:

!(fig_tree)("images/tree.png")

### Setup constants

- In a separate file, `constants.py`, set the following constants:

BTC = 'btc'\
ETH = 'eth'\
BTCTEST = 'btc-test'
  
### Generate a Mnemonic

- Generate a **new** 12 word mnemonic using `hd-wallet-derive` or by using [this tool](https://iancoleman.io/bip39/).

- Set this mnemonic as an environment variable by storing it a an `.env` file and importing it into your `wallet.py`.

--------------------------------------------------------------------------------------------------------


## 1.  Setting up two nodes for local network - Proof Of Work (POW setup)

Follow these steps:

Open terminal. cd into the Blockchain-Tools folder and run the following commands (one by one)

#### ./geth --datadir node1 account new   
(it will prompt you for a password. Add password. Make sure to write and save it for later usage. Plus Copy and Paste - use notebook, we will use this in later steps - "Public address of the key" and "Path of the secret key file") 

#### ./geth --datadir node2 account new
(it will prompt you for a password. Add password. Make sure to write or save it for later usage. Plus Copy and Paste - use notebook, we will use this in later steps - "Public address of the key" and "Path of the secret key file") 

## 2. Next, generate your genesis block.

Enter the following command - You could use same terminal window or close the existing terminal window, and open a new one (Make sure to cd into the correct folder, Blockchain-Tools).
#### ./puppeth

## 3. name your network 
specify any network name (no "spaces", "hyphens" or "capital letters" please) - save this for later reference/usage)

## 4. select the option to configure a new genesis block. 
####  ENTER 2 
"Configure new genesis"

## 5. What would you like to do? 
####  ENTER 1
"Create new genesis from scratch"

## 6. Which consensus engine to use? 
####  ENTER 1
"Ethash - proof-of-work"

## 7. Which accounts should be pre-funded?
#### 0X-----------------
We need to fetch "Public address of the key" (minus "OX"), which we saved in step 1 above for node1. Hit 
Enter
#### 0X-----------------
just Hit Enter - we only need to fund the first account

## 8. Should the precompile-addresses (0x1 .. 0xff) be pre-funded with 1 wei? (advisable yes)
Hit Enter

## 9. Specify your chain/network ID if you want an explicit one

*** IMPORTANT ** use the first six letters of "public address of the key" from step 1 above (including "OX"), and convert it to a decimal value.
Here is a link which you could leverage for converting hex-to-decimal value
https://www.rapidtables.com/convert/number/hex-to-decimal.html

#### Enter the decimal value you obtained after converting first six letters of public address
save this value for later usage

## 10. What would you like to do?
#### Enter 2
"Manage existing genesis"

#### Enter 2 
Export genesis configurations

## 11. Which folder to save the genesis specs into?
#### Hit Enter
Export genesis configurations. 
This should create four ".json" files in Blockchain-Tools folder

This completes genesis block creation. Use ("command+." or "control+c") to terminate session, and close the terminal window.

Please open your "Blockchain-Tools" folder. You should have node1 and node2 folders, and four (*.json) files.
-------------------------------------------------------------------------------------------------------


## 12. Initialize the nodes with the genesis' json file
open a new terminal window. cd into the Blockchain-Tools folder and run the following commands (one by one)

#### ./geth --datadir node1 init networkname.json
Replace "networkname" with your own network name from step 3.

#### ./geth --datadir node2 init networkname.json
Again, replace "networkname" with your own network name from step 3.

This will initialize your two nodes.
Close the terminal window.

-------------------------------------------------------------------------------------------------------

## 13. Start mining blocks nodes
open a new terminal window. cd into the Blockchain-Tools folder and run the following command

#### ./geth --datadir node1 --mine -minerthreads 1
scroll up and search for the following:
"enode://xxxx----------------------------------------------------------------------xxxxx@127.0.0.1:30303"
please copy this in notebook, we are going to need the above code for node2 (copy everything upto @IP address)

open a second terminal window. cd into the Blockchain-Tools folder and run the following command
#### ./geth --datadir node2 --port 30304 --rpc --bootnodes "ABOVE encode://.........."
Replace, "ABOVE encode://..........", with info that you copy from previous step.   


Your private proof-of-work (POW) blockchain should now be running!

-------------------------------------------------------------------------------------------------------

## MyCrypto APP (set up your own network)
With both nodes up and running, the blockchain can be added to MyCrypto for testing.

#### Open the MyCrypto app, then click `Change Network` at the bottom left: 

#### Click "Add Custom Node". It should open a new pop-up window "Set Up your Custom Network"  

#### Use dropdown option in "Network" and select "Custom"

#### Enter same network name for "Node Name" and "Network Name"
please make sure to enter same network name that you saved in step 3

#### For "Currency", type "ETH"

#### For "Chain ID", type decimal value from step 9

#### For "URL", Type "http://127.0.0.1:8545"

#### Finally, click "Save & Use Custom Node"
Make sure your new custom node is selected at the bottom left

#### Select "View & Send" option from the left menu pane, then click "Keystore file"

#### On the next screen, click "Select Wallet File", then navigate to the keystore directory inside your Node1 directory (in Blockchain-Tools folder), select the file located there, provide your password (that you saved in step 1) when prompted and then click "Unlock".

This will open your account wallet inside MyCrypto.
If you follow the steps correctly, you should have plenty of money in this wallet

Now, you are ready to make transactions using your local network through python code! 
