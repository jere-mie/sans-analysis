# Running Jupyter Notebooks in Google Colab

You can utilize any of the code (especially from the `calculations` module) in Jupyter notebooks

Simply add the following to the beginning of the notebook: 

```sh
!git clone https://github.com/jere-mie/sans-analysis
!cd /content/sans-analysis/ && git pull
import sys
sys.path.append('/content/sans-analysis')
# downloading the bin file used for figure 7 (stored on google drive) 
!gdown https://drive.google.com/uc?id=143UUSiW2jtNOt5YlVu08aaut43ZK9EPX
```

Then you can import and use things like so:

```py
import calculations.matrices as mt
F = mt.generateFPrompt()
# or
F = mt.readFBin('data-fig-7.bin', (200, 101, 1150))
```