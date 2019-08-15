# Team

## Contributors

_pandas_ is made with love by more than [1,500 volunteer contributors](https://github.com/pandas-dev/pandas/graphs/contributors).

If you want to support pandas development, you can find information at the [Donate page](../donate.html).

## Maintainers

<div class="maintainers">
    {% for row in maintainers.people | batch(5) %}
        <div class="card-deck maintainers">
            {% for person in row %}
                <div class="card">
                    <img class="card-img-top" alt="" src="{{ person.avatar_url }}"/>
                    <div class="card-body">
                        <h5 class="card-title"><a href="{% if person.blog %}{{ person.blog }}{% else %}{{ person.html_url }}{% endif %}" target="_blank">{{ person.name }}</a></h5>
                        <p class="card-text">{{ person.login }}</p>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% endfor %}
</div>

## BDFL

Wes McKinney is the Benevolent Dictator for Life (BDFL).

## Governance

The project governance is available in the [governance document](governance.html).

## NumFOCUS

![](https://numfocus.org/wp-content/uploads/2018/01/optNumFocus_LRG.png)

_pandas_ is a Sponsored Project of [NumFOCUS](https://numfocus.org/), a 501(c)(3) nonprofit charity in the United States.
NumFOCUS provides _pandas_ with fiscal, legal, and administrative support to help ensure the
health and sustainability of the project. Visit numfocus.org for more information.

Donations to _pandas_ are managed by NumFOCUS. For donors in the United States, your gift is tax-deductible
to the extent provided by law. As with any donation, you should consult with your tax adviser about your particular tax situation.

## Code of conduct committee

- Safia Abdalla
- Tom Augspurger
- Joris Van den Bossche
- Camille Scott
- Nathaniel Smith

## NumFOCUS committee

- Phillip Cloud
- Stephan Hoyer
- Wes McKinney
- Jeff Reback
- Joris Van den Bossche

## Institutional partners

- [Anaconda, Inc.](https://www.anaconda.com/) (Tom Augspurger, Brock Mendel)
- [Two Sigma](https://www.twosigma.com/) (Phillip Cloud, Jeff Reback)
- [RStudio](https://www.rstudio.com) (Wes McKinney)
- [Ursa Labs](https://ursalabs.org) (Wes McKinney, Joris Van den Bossche)

In-kind sponsors

- [Indeed](https://opensource.indeedeng.io/): Logo and website design
- Can we find a donor for the hosting (website, benchmarks,...?)

## Emeritus maintainers

- Wouter Overmeire
- Skipper Seabold
- Jeff Tratner

## Emeritus corporate sponsors

- [Paris-Saclay Center for Data Science](https://www.datascience-paris-saclay.fr/)
