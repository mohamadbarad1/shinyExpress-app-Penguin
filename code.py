from palmerpenguins import load_penguins
from plotnine import ggplot, aes, geom_histogram, theme_minimal

dat = load_penguins()

species = "Gentoo"
sel = dat.loc[dat.species ==species]
 

(    ggplot(aes(x='bill_length_mm'))
     + geom_histogram(dat, fill = "#C2C2C4",binwidth=1)
     + geom_histogram(sel, fill = "#447099",binwidth=1)
     + theme_minimal()
)
