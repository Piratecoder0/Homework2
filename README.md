# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
tokenB->tokenA 
    amountIn:5
    amountOut:5.655321988655322

tokenA->tokenE 
    amountIn:5.655321988655322
    amountOut:1.0583153138066885

tokenE->tokenD 
    amountIn:1.0583153138066885
    amountOut:2.4297862601422264

tokenD->tokenC 
    amountIn:2.4297862601422264
    amountOut:5.038996197252911

tokenC->tokenB 
    amountIn:5.038996197252911
    amountOut:20.042339589188174

final reward:20.042339589188174

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
Slippage refers to the deviation between the intended transaction price and the actual executed price in a trade.Uniswap V2, a popular decentralized exchange (DEX), uses the constant product market maker model.In this model, the product of the two asset quantities (usually denoted as xy=k) remains constant to facilitate market transactions.
function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external virtual override ensure(deadline) returns (uint[] memory amounts) {
        amounts = UniswapV2Library.getAmountsOut(factory, amountIn, path);
        require(amounts[amounts.length - 1] >= amountOutMin, 'UniswapV2Router: INSUFFICIENT_OUTPUT_AMOUNT');
        TransferHelper.safeTransferFrom(
            path[0], msg.sender, UniswapV2Library.pairFor(factory, path[0], path[1]), amounts[0]
        );
        _swap(amounts, path, to);
    }

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
Minimum Liquidity Requirement:
During initial liquidity minting, a minimum liquidity is subtracted from the total minted amount.
This design choice serves several purposes:
1. Preventing Exploits: Without this minimum, an attacker could manipulate the system by depositing a tiny amount of tokens and minting a large number of liquidity tokens. This would distort the pool’s reserves and affect subsequent trades.
2. Fair Distribution: By subtracting a minimum, Uniswap ensures that liquidity providers contribute a reasonable amount of tokens to the pool. It prevents excessive minting by users who deposit negligible amounts.
3. Balancing Liquidity: The minimum liquidity requirement helps maintain a balanced pool, ensuring that the initial liquidity is meaningful and contributes to efficient trading.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
This formula is aimed at ensuring stability in the ratio of the two tokens. By using a specific formula (x*y=k), the addition of new liquidity tokens can maintain an appropriate proportion with the existing liquidity tokens. This helps prevent one asset from becoming too scarce or too abundant, ultimately enhancing the efficiency and stability of the transactions.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack occurs when an attacker exploits the predictable behavior of pending transactions to manipulate the execution price of a swap.
Suppose a user (the victim) submits a swap transaction to buy or sell tokens.
The attacker monitors the pending transactions and identifies the victim’s trade.
The attacker then quickly submits their own transactions:
Front-Running: The attacker places a transaction to buy or sell the same tokens just before the victim’s transaction.
Back-Running: The attacker follows up with another transaction to reverse the initial trade.
The victim’s transaction executes at a less favorable price due to the sudden price movement caused by the attacker’s trades.

