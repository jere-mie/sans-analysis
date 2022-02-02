# High Level Workflow

**Note**: dimensions are in Y by X by Z (down, right, inward)  
**Note**: this workflow creates the heterogeneous I(q) vector. Details on the homogeneous intensity contribution can be found [here](https://media.discordapp.net/attachments/937419611622752277/937428080438427668/unknown.png).

## Step 1

1. F Matrix (QxRxL) is dotted by Omega matrix (RxS)
    - Resultant is denoted as W' (QxSxL)
    - [How we calculate the F matrix](f-matrix.md)
    - [How we calculate the Omega, Theta, D and M matrices](scattering-length-density-matrices.md)
2. We transpose W' (QxSxL) to make W (QxLxS)

![Step 1 Image](https://media.discordapp.net/attachments/937419611622752277/937420728637194280/unknown.png)

## Step 2

1. We take the absolute square of the W matrix (QxLxS) to create $|W|^2$
2. We dot the $|W|^2$ matrix (QxLxS) with the squared angular coefficient vector (denoted as $|w~|^2$) (L)
    - Resultant is the monodisperse I(q) matrix (denoted as P) (Qx1xS or just QxS)
    - [How we get the w~ vector](w-vector.md)

![Step 2 Image](https://media.discordapp.net/attachments/937419611622752277/937421849204260924/unknown.png)

## Step 3

1. P matrix (QxS) is dotted with Schulz weights vector (denoted as s) (S)
    - Resultant is polydisperse I(q) vector (Qx1)

![Step 3 Image](https://media.discordapp.net/attachments/937419611622752277/937422667189997598/unknown.png)

## Appendix

### Matrix Dimensions

![matrix dimensions](https://media.discordapp.net/attachments/937419611622752277/937422892382167080/unknown.png)

### Workflow Description

1. Compute radial form factor matrix
2. Combnie radial, angular information to compute monodisperse I(q) matrix
3. Perform Schulz averaging to obtain polydisperse I(q)

### Some Notable Scalars and Vectors

**Note**: a square around a term means it is precomputed and stored  

![Workflow Specific](https://media.discordapp.net/attachments/937419611622752277/937424763675095050/unknown.png)
![Scalars and Vectors](https://media.discordapp.net/attachments/937419611622752277/937423790848245770/unknown.png)

### Entire Slide

![workflow slide](https://media.discordapp.net/attachments/937419611622752277/937896015766380584/unknown.png)
