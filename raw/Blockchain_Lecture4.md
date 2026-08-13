# Blockchain Lecture 4

## Slide 1

Part 3

## Slide 2

Hedera


         Connect With Me On Twitter | @HendrikEbbers

## Slide 3

Hedera


         Connect With Me On Twitter | @HendrikEbbers

## Slide 4

The next generation




1st generation   2nd generation           3rd generation



                                  Connect With Me On Twitter | @HendrikEbbers

## Slide 5

The Hedera Network
•The Hedera Network is a network that is based on
 several nodes
•Nodes running on machines of the Hedera Foundation
 council members




                                           Connect With Me On Twitter | @HendrikEbbers

## Slide 6

*(no extractable text — image-only slide)*

## Slide 7

Sustainability of Hedera
•0.000003 kWh per transaction
    0.006 kWh at Ethereum

•Hedera is committed to carbon-negative network
 operations by purchasing carbon offsets quarterly




                                               Connect With Me On Twitter | @HendrikEbbers

## Slide 8

Hedera Network facts
•> 40,000,000 transactions per day
    1,000,000 at Ethereum

•0.001$ cost per transaction
 1.72 $ at Ethereum

•0.000003 kWh per transaction
  0.006 kWh at Ethereum
                                     Connect With Me On Twitter | @HendrikEbbers

## Slide 9

Hedera Network facts
•MainNet can handle > 1.000 tps
 (transaction per second)
•Over 35.000.000.000 transactions have
 been handled in production
•In near future it will be > 50 Billion
 transactions
                                              https://hederatxns.com/


                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 10

*(no extractable text — image-only slide)*

## Slide 11

Sustainability of Hedera
                                                                         Hedera




                            From Proof-of-Work to
                                Proof-of-Stake




   Bitcoin   Ethereum 1.o                     Ethereum 2.o
                                              Connect With Me On Twitter | @HendrikEbbers

## Slide 12

The Hedera Network
•The productive network is called MainNet
•Hedera provides TestNet and PreviewNet networks for
 development and testing




MainNet           TestNet        PreviewNet

                                            Connect With Me On Twitter | @HendrikEbbers

## Slide 13

The Hedera Network
•A local network can be setup by using the open source local
 node project that is based on Docker




                                                      [ [
 http://bit.ly/3JqeMvz




MainNet             TestNet         PreviewNet                LocalNode

                                                Connect With Me On Twitter | @HendrikEbbers

## Slide 14

The Hedera Documentation




                              Scan for URL




                                  @net0pyr | @hendrikEbbers
                                                    SwirldsLabs.com
                           © 2023 Swirlds Labs Inc. All rights reserved

## Slide 15

Hedera Testnet


           Connect With Me On Twitter | @HendrikEbbers

## Slide 16

Hedera Testnet
•We do not want to execute our contracts on the real Hedera
 ledger at development time
•Hedera provides a test instance - Hedera Testnet
     https://docs.hedera.com/guides/testnet/testnet-access



                                                                           10,000 HBAR
                                                                              per day
                            public api



                                               Hedera Testnet

                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 17

Hedera Testnet




                                        Scan for URL




                 Connect With Me On Twitter | @HendrikEbbers

## Slide 18

Development
 Workflow

         Connect With Me On Twitter | @HendrikEbbers

## Slide 19

Deploying a smart contract
•To execute a smart contract we need to deploy it on a ledger
•Public ledgers like Ethereum or Hedera provide public APIs
 to interact with the ledger




                          public api




                                                Connect With Me On Twitter | @HendrikEbbers

## Slide 20

HAPI - Hedera API
•Rich documentation available online
   https://docs.hedera.com/guides/docs/hedera-api


•API libraries available for several languages



                   [                  ]             In development
                                                 Connect With Me On Twitter | @HendrikEbbers

## Slide 21

HAPI - Hedera API
•We will concentrate on Java
  <dependency>
     <groupId>com.hedera.hashgraph</groupId>
     <artifactId>sdk</artifactId>
     <version>2.17.0</version>
  </dependency>




•All Hedera sources can be found at GitHub
  https://github.com/hashgraph/hedera-sdk-java


                                                 Connect With Me On Twitter | @HendrikEbbers

## Slide 22

Hedera Testnet
•We do not want to execute our contracts on the real Hedera
 ledger at devolpment time
•Hedera provides a test instance - Hedera Testnet
    https://docs.hedera.com/guides/testnet/testnet-access



                                                                           10,000 HBAR
                                                                              per day
                           public api



                                               Hedera Testnet

                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 23

Connect With Me On Twitter | @HendrikEbbers

## Slide 24

Connect With Me On Twitter | @HendrikEbbers

## Slide 25

HAPI - Smart contracts
•For executing a smart contract we need do the following
 steps:
 •Connect to the ledger
 •Upload the compiled contract to the ledger
 •Create a smart contract out of the binary
 •Call a function of the smart contract

                                               Connect With Me On Twitter | @HendrikEbbers

## Slide 26

HAPI - Deploy a smart contract
final ContractCreateFlow flow = new ContractCreateFlow()
       .setBytecode(bytecodeInHex)
       .setGas(1_000_000);



                             ??
final TransactionResponse transactionResponse = flow.execute(client);
final TransactionReceipt receipt = transactionResponse.getReceipt(client);
return receipt.contractId;



                                                           Connect With Me On Twitter | @HendrikEbbers

## Slide 27

HAPI - Connect to the ledger
                                                                                Network properties
final String consensusNodeAddress = getProperty("hedera.consensusNode.address");
final AccountId consensusNodeId = AccountId.fromString(getProperty("hedera.consensusNode.id"));
final String mirrorNodeAddress = getProperty("hedera.mirrorNode.address");


final String operatorId = getProperty("hedera.operator.id");
                                                                      Account properties
final String operatorKey = getProperty(„hedera.operator.key");




final Client client = Client.forNetwork(
                      Collections.singletonMap(consensusNodeAddress, consensusNodeId)).setMirrorNetwork(
                      List.of(mirrorNodeAddress));
client.setOperator(AccountId.fromString(operatorId), PrivateKey.fromString(operatorKey));


                                                                             Connect With Me On Twitter | @HendrikEbbers

## Slide 28

HAPI - File upload
                                                               Request
byte[] bytecode = readCompiledContract();
FileCreateTransaction fileCreateTx = new FileCreateTransaction()
fileCreateTx.setContents(bytecode);




TransactionResponse response = fileCreateTx.execute(client);
FileId fileId = response.getReceipt(client).fileId;


                                                        Response

                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 29

HAPI - Create smart contract
ContractCreateTransaction contractTx = new ContractCreateTransaction()
                  .setBytecodeFileId(fileId)
                  .setGas(100_000);



                                     de f i n e m a x g as c os t
                       We n e e d to

TransactionResponse contractResponse = contractTx.execute(client);
ContractId contractId = contractResponse.getReceipt(client).contractId;




                                                                    Connect With Me On Twitter | @HendrikEbbers

## Slide 30

HAPI - call contract function
final ContractCallQuery contractQuery = new ContractCallQuery()
                 .setGas(100000)
                 .setContractId(contractId)
                 .setFunction("greet");




ContractFunctionResult result = contractQuery.execute(client);




                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 31

HAPI - Transactions in general
//Create the transaction and set the transaction properties


Transaction transaction = new AccountCreateTransaction() //Any transaction can be applied here
     .setKey(key)
     .setInitialBalance(Hbar.fromTinybars(1000))
     .setMaxTransactionFee(new Hbar(2)) //Set the max transaction fee to 2 hbar
     .setTransactionMemo("Transaction memo"); //Set the node ID to submit the transaction to




      https://docs.hedera.com/hedera/sdks-and-apis/sdks/transactions/modify-transaction-fields


                                                                       Connect With Me On Twitter | @HendrikEbbers

## Slide 32

HAPI - Getting started
public class HederaExamples {

        public static void main(String[] args) {

                //Grab your Hedera Testnet account ID and private key
                AccountId myAccountId = AccountId.fromString(Dotenv.load().get("MY_ACCOUNT_ID"));+
                PrivateKey myPrivateKey = PrivateKey.fromString(Dotenv.load().get("MY_PRIVATE_KEY"));
                //Create your Hedera Testnet client

                Client client = Client.forTestnet();
                client.setOperator(myAccountId, myPrivateKey);

                // Set default max transaction fee & max query payment
                client.setDefaultMaxTransactionFee(new Hbar(100));
                client.setMaxQueryPayment(new Hbar(50));
    }
}
                  https://docs.hedera.com/hedera/getting-started/environment-set-up


                                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 33

web3j
•Next to the Hedera SDK the web3j lib can be used
•web3j has been created for Ethereum
•Based on standards or widely adapted functionality it can be
 used for Hedera




                                                Connect With Me On Twitter | @HendrikEbbers

## Slide 34

web3j
•web3j provides API to interact with smart contracts
•web3j provides functionality to create Java wrappers for
 smart contracts
•web3j provides wrapper for smart contract compilation
•web3j provides Maven plugin


                                               Connect With Me On Twitter | @HendrikEbbers

## Slide 35

Hedera & Solidity
•Precompiled services: https://github.com/
 hashgraph/hedera-smart-contracts/
•Hedera Solidity tutorials & documentation: https://
 docs.hedera.com/hedera/tutorials/smart-
 contracts




                                            Connect With Me On Twitter | @HendrikEbbers

## Slide 36

Voting Contract
    Sample

            Connect With Me On Twitter | @HendrikEbbers

## Slide 37

Voting Contract
•Transparent and secure voting is often mentioned as a use
 case for smart contracts
•Let's have a look how such contract might look



                                                            VOTE

                                                  Connect With Me On Twitter | @HendrikEbbers

## Slide 38

Voting Contract V1
•Setup proposals
                       pragma solidity >= 0.7.0 <0.9.0;

                       contract Poll {

•Vote for a proposal       constructor(bytes32[] memory proposalNames) {


•Show winner
                           function vote(uint proposal) public {}

                           function winner() public view returns (bytes32 result) {}
                       }




                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 39

Data Structure
                            pragma solidity >= 0.7.0 <0.9.0;


•Proposal has name and      contract Poll {


 counter
                                struct Proposal {
                                    bytes32 name;
                                    uint count;
                                }

•Several proposals stored       Proposal[] public proposals;

 in array                       constructor(bytes32[] memory proposalNames) {}

                                function vote(uint proposal) public {}

•Proposals are publicly     }
                                function winner() public view returns (bytes32 result) {}


 readable



                                                       Connect With Me On Twitter | @HendrikEbbers

## Slide 40

Setup proposals
                             pragma solidity >= 0.7.0 <0.9.0;


•Iterate over all proposal   contract Poll {


 names
                                 ...

                                 constructor(bytes32[] memory proposalNames) {
                                     for (uint i = 0; i < proposalNames.length; i++) {

•Create a Proposal                       Proposal memory proposal = Proposal({
                                             name: proposalNames[i],
                                             count: 0


•Add the proposal to the
                                         });
                                         proposals.push(proposal);
                                     }

 proposal-array
                                 }

                                 function vote(uint proposal) public {}

                                 function winner() public view returns (bytes32 result) {}
                             }




                                                        Connect With Me On Twitter | @HendrikEbbers

## Slide 41

Vote for a proposal
                        pragma solidity >= 0.7.0 <0.9.0;


•Increase the counter   contract Poll {

                            ...

                            constructor(bytes32[] memory proposalNames) {}

                            function vote(uint proposal) public {
                                proposals[proposal].count++;
                            }

                            function winner() public view returns (bytes32 result) {}
                        }




                                                   Connect With Me On Twitter | @HendrikEbbers

## Slide 42

Show winner
                              pragma solidity >= 0.7.0 <0.9.0;


•Iterate over all proposals   contract Poll {

                                  ...

•Find proposal with most          constructor(bytes32[] memory proposalNames) {}


 votes                            function vote(uint proposal) public {}

                                  function winner() public view returns (bytes32 result) {


•Check condition:
                                      result = "";
                                      ...




                                                ?
 if (condition) {}
                                  }
                              }




                                                         Connect With Me On Twitter | @HendrikEbbers

## Slide 43

Show winner
                              pragma solidity >= 0.7.0 <0.9.0;


•Iterate over all proposals   contract Poll {

                                  ...

•Find proposal with most          constructor(bytes32[] memory proposalNames) {}


 votes                            function vote(uint proposal) public {}

                                  function winner() public view returns (bytes32 result) {


•Check condition:
                                      result = "";
                                      uint maxCount = 0;
                                      for (uint i = 0; i < proposals.length; i++) {

 if (condition) {}
                                          if (proposals[i].count > maxCount) {
                                              maxCount = proposals[i].count;
                                              result = proposals[i].name;
                                          }
                                      }
                                  }
                              }




                                                         Connect With Me On Twitter | @HendrikEbbers

## Slide 44

Voting Contract V2
•Authorize voters
•One vote per user




                     Connect With Me On Twitter | @HendrikEbbers

## Slide 45

Setup admin
                               pragma solidity >= 0.7.0 <0.9.0;


•Creator of contract           contract Poll {


 becomes admin
                                   address public admin;

                                   ...


•Users identified by address       constructor(bytes32[] memory proposalNames) {
                                       admin = msg.sender;
                                       ...


•msg contains metadata
                                   }

                                   function vote(uint proposal) public {}

 of message                    }
                                   function winner() public view returns (bytes32 result) {}




                                                           Connect With Me On Twitter | @HendrikEbbers

## Slide 46

Safeguard vote()
                                  pragma solidity >= 0.7.0 <0.9.0;


•Voter can have one of three      contract Poll {


 states
                                      enum VoterState { NotAuthorized, Authorized, Voted }

                                      mapping(address => VoterState) public voters;


•State for all voters is stored       ...

                                      constructor(bytes32[] memory proposalNames) {}
 in mapping                           function vote(uint proposal) public {
                                          require(

•require checks condition
                                              voters[msg.sender] == VoterState.Authorized,
                                              "Not authorized“
                                          );

                                            voters[msg.sender] = VoterState.Voted;
                                            proposals[proposal].count++;
                                      }

                                      function winner() public view returns (bytes32 result) {}
                                  }



                                                               Connect With Me On Twitter | @HendrikEbbers

## Slide 47

Authorize users
                            pragma solidity >= 0.7.0 <0.9.0;


•Only admin can authorize   contract Poll {


 voters
                                ...

                                constructor(bytes32[] memory proposalNames) {}


•Only unauthorized users        function vote(uint proposal) public {}

                                function winner() public view returns (bytes32 result) {}
 can be authorized              function authorize(address voter) public {




                                              ?
                                }
                            }

                                                       Connect With Me On Twitter | @HendrikEbbers

## Slide 48

Authorize users
                            pragma solidity >= 0.7.0 <0.9.0;


•Only admin can authorize   contract Poll {


 voters
                                ...

                                constructor(bytes32[] memory proposalNames) {}


•Only unauthorized users        function vote(uint proposal) public {}

                                function winner() public view returns (bytes32 result) {}
 can be authorized              function authorize(address voter) public {
                                    require(
                                        msg.sender == admin,
                                        "Only admin can authorize"
                                    );
                                    require(
                                        voters[voter] == VoterState.NotAuthorized,
                                        "Already authorized"
                                    );

                                      voters[voter] = VoterState.Authorized;
                                }
                            }

                                                         Connect With Me On Twitter | @HendrikEbbers

## Slide 49

Our GitHub Repository




                                               Scan for URL




                        Connect With Me On Twitter | @HendrikEbbers

## Slide 50

Coins & Tokens


           Connect With Me On Twitter | @HendrikEbbers

## Slide 51

Smart Contracts and Tokens
•Ethereum (and the EVM) allows
 you to define any kind of token
•Non-Fungible Tokens (NFTs) are
 supported
•Tokens and NFTs are based on
 smart contracts



                                   Connect With Me On Twitter | @HendrikEbbers

## Slide 52

Smart Contracts and Tokens
 Fungible          Non-Fungible
 •Interchangable   •Interchangable
 •Divisible        •Divisible
 •Uniform          •Uniform



                            Connect With Me On Twitter | @HendrikEbbers

## Slide 53

What is a fungible token?
               Contract (ERC-20)
  Token
                totalSupply(): uint256

   address      balanceOf(address): uint256

   id           transfer(address, uint256): bool

                allowance(address, address): uint256

                approve(address, uint256): bool

                transferFrom(address, address, uint256): bool




                                         Connect With Me On Twitter | @HendrikEbbers

## Slide 54

What is a non-fungible token?
               Contract (ERC-721)
  Token
                balanceOf(owner): balance

                ownerOf(tokenId): owner
   address
                safeTransferFrom(from, to, tokenId, data)
   id
                transferFrom(from, to, tokenId)

                approve(to, tokenId)

                setApprovalForAll(operator, approved)

                getApproved(tokenId): operator

                isApprovedForAll(owner, operator): bool




                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 55

Contract code for tokens




                                             Scan for URL




                      Connect With Me On Twitter | @HendrikEbbers

## Slide 56

Coin or Token
•Coin: Created as native assets on their independent
 blockchains (e.g., Bitcoin on the Bitcoin blockchain).
•Token: Issued on existing blockchain platforms, utilizing the
 infrastructure of blockchain projects like Ethereum or
 Hedera.




                                                  Connect With Me On Twitter | @HendrikEbbers

## Slide 57

Coin or Token
•Coin: Created through a process like mining (for
 cryptocurrencies like Bitcoin).
•Token: Easily created through smart contracts on platforms
 that support token creation, without the need to develop a
 separate blockchain.




                                                Connect With Me On Twitter | @HendrikEbbers

## Slide 58

Stable Coins
•Value Stability: Designed to have a stable value, as opposed
 to the high volatility seen in most cryptocurrencies.
•Pegged Value: Often pegged to a stable asset, such as a
 specific amount of a fiat currency or a commodity like gold.
•Types: Can be classified into various types, including fiat-
 collateralized, crypto-collateralized, and algorithmic stable
 coins.

                                                  Connect With Me On Twitter | @HendrikEbbers

## Slide 59

Stable Coins
•Tether (USDT): A fiat-collateralized stable coin, pegged
 to the US Dollar, widely used in the cryptocurrency
 market.
•USD Coin (USDC): A fully-backed digital dollar issued by
 regulated financial institutions.
•Binance USD (BUSD): A stable coin pegged to the US
 Dollar, issued in partnership between Binance and Paxos
  These are a few examples of stable coins, each having unique features and backed by different
  mechanisms to maintain their stability.
                                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 60

Tokens
Stable Coins
                                                                       Token
•Tether (USDT): A fiat-collateralized stable coin, pegged
 to the US Dollar, widely used in the cryptocurrency
 market.
•USD Coin (USDC): A fully-backed digital dollar issued by
 regulated financial institutions.
•Binance USD (BUSD): A stable coin pegged to the US
 Dollar, issued in partnership between Binance and Paxos
  These are a few examples of stable coins, each having unique features and backed by different
  mechanisms to maintain their stability.
                                                                          Connect With Me On Twitter | @HendrikEbbers

## Slide 61

USDC                                Available as token
                                             all that networks o n




https://www.circle.com/en/usdc/developers   Connect With Me On Twitter | @HendrikEbbers

## Slide 62

USDC                                               Test it on Hedera




https://www.circle.com/en/usdc-multichain/hedera   Connect With Me On Twitter | @HendrikEbbers

## Slide 63

USDC                                  Solidity files at Git
                                                                    hu                        b




https://github.com/circlefin/stablecoin-evm     Connect With Me On Twitter | @HendrikEbbers

## Slide 64

USDC                                                            Check the deployed
                                                                                                              contract




https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48         Connect With Me On Twitter | @HendrikEbbers

## Slide 65

Working with tokens / coins
•Sending coins: https://docs.soliditylang.org/en/
 v0.8.23/units-and-global-
 variables.html#members-of-address-types
•Precompiled services for Hedera: https://github.com/
 hashgraph/hedera-smart-contracts/
•Security Pattern: https://docs.soliditylang.org/
 en/v0.8.23/common-patterns.html#restricting-
 access
                                           Connect With Me On Twitter | @HendrikEbbers

## Slide 66

Token Workshop




                                        Scan for URL




                 Connect With Me On Twitter | @HendrikEbbers
