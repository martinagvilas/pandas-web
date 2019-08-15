# Team

## Contributors

_pandas_ is made with love by more than [1,500 volunteer contributors](https://github.com/pandas-dev/pandas/graphs/contributors).

If you want to support pandas development, you can find information at the [Donate page](../donate.html).

## Maintainers

<div class="team">
    {% for person in maintainers.people %}
        <div class="team-member">
            <img alt="" src="{{ person.avatar_url }}"/>
            <p><a href="{% if person.blog %}{{ person.blog }}{% else %}{{ person.html_url }}{% endif %}">{{ person.name }}</a></p>
            <p>{{ person.login }}</p>
        </div>
    {% endfor %}
</div>

## BDFL

Wes McKinney is the Benevolent Dictator for Life (BDFL).

## Governance

The project governance is available in the [governance document](governance.html).

## NumFOCUS

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

- [Indeed](https://opensource.indeedeng.io/)
- Can we find a donor for the hosting (website, benchmarks,...?)

## Emeritus maintainers

- Wouter Overmeire
- Skipper Seabold
- Jeff Tratner

## Emeritus corporate sponsors

- [Paris-Saclay Center for Data Science](https://www.datascience-paris-saclay.fr/)
