# Team

WIP

Content:

- List of active core developers
- Project governance information
- Mention about volunteering work and link to donate
- List of companies that employ core developers to work on pandas
- Members of the committees
- Emeritus core devs and companies that employ core devs

Some of the info can be found at <https://github.com/pandas-dev/pandas-governance/blob/master/people.md> (and in the website)

_pandas_ is made with love by >1,500 volunteer contributors, and maintained by the next people:

<div class="team">
    {% for person in maintainers.people %}
        <div class="team-member">
            <img alt="" src="{{ person.avatar_url }}"/>
            <p><a href="{% if person.blog %}{{ person.blog }}{% else %}{{ person.html_url }}{% endif %}">{{ person.name }}</a></p>
        </div>
    {% endfor %}
</div>
