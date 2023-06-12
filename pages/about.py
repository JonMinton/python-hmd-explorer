import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div(
        [
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Origins")),
                    dbc.CardBody(
                        dcc.Markdown(
                            """
        This app is based on a previous app I produced using R Shiny a number of years ago. 
        The earlier app is still available [here](https://datascapes.shinyapps.io/hmd_explorer/) and focuses on 3D (Lexis surface) visualisations 
        of demographic data.                     
                            """
            
                        )
                    )

                ],
                className = "mb-3"

            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Differences from previous version")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        This app is written using Python and Dash. The previous app was written using R and Shiny.

        Python (according to ChatGPT) is a high-level programming languate known 
        for its simplicity, readability, and versatility. 
        In addition it appears to be much more widely use than R for data science purposes. 
        (Although R is still widely used throughout much of academia, in my experience.)

        Dash is (according to ChatGPT) a Python-based framework that allows developors to easily build web
        applications with highly interactive user interfaces, and is expecially population for data 
        visualisation web applications. Dash offers pre-built components for creating 
        interactive web pages, including HTML, CSS, and JavaScript. But does this 
        without the coder having to work directly in languages other than 
        Python. 
        From my perspective, **Dash is to Python as Shiny is to R**. 

        Aside from these differences in languages, I intend that this app will include greater 
        functionality, including some simpler 2D visualisations of data, such as life expectancy against time, 
        and hopefully a better presentation and user experience overall.        
        
        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Similarities to previous version")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        Ultimately, the main visualisions produced in the previous app were made using [Plotly](https://plotly.com/), and I expect this 
        app will mainly use Plotly too. 

        Plotly is a data visualisation graphical library that allows developers to create 
        interactive and customisable graphs, charts and plots from a range of other languages, including 
        through its [Python](https://plotly.com/python/) and [R](https://plotly.com/r/) libraries. This includes [3D surface plots](https://plotly.com/python/3d-surface-plots/), 
        which this app makes extensive use of. 

        Plotly is written in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), and builds on the low level Javascript graphical interface [D3](https://d3js.org/). 
        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("What is Demography?")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
       Demography is the scientific studies of human populations, including their size, 
       structure, distribution, and how they change over time, 
      both across time and place. 
      The term 'demography' is derived from the Greek words 'demos', meaning 'people', and 'graphy', meaning 'description'. 

        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("What is a Lexis surface?")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        A Lexis surface is a graphical representation of demographic data, showing visually how a demographic quantity varies 
        jointly by age, period and cohort. It is usually displayed with age across the x axis ('depth'), period (time) across the y axis ('width')
        and a demographic quantity (such as population size or force of mortality) along the third x axis ('height'). 
        Within this representation, and if both the age and period use an equal ratio (i.e. an additional year is an equal distance over the period axis as the 
        age axis), then birth cohorts are apparent at 45 degree diagonals along the age-period plane.         
        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("What is a Lexis diagram?")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        A Lexis diagram is a graphical way of representing and thinking about demographic events in terms of individual life trajectories. 
        On a Lexis diagram, the horizontal (x) axis can be used to represent time (period), and the vertical (y) axis used to 
        represent age. If the oldest periods are on the left side of the graph, and the youngest ages at the bottom of the graph, and an equal 
        scale used for both the x and y axes, then an individual life trajectory can be represented as diagonal line running at 
        45 degrees from the bottom of the graph and moving upwards and to the right. 

        At various specific ages an individual, represented by a diagonal line, may experience a life event, such as marriage or death. 
        Such events can be represented by placing a symbol on the lifelines at the exact age at which they occur. For the final event, death, the 
        lifeline tends not to extend beyond the symbol representing the event.         
        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("What are Lexis squares and Lexis triangles?")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        Given a well populated Lexis diagram, we can imagine drawing regular gridlines, say at one year by one year intervals, across bot the 
        horizontal and vertical axes. These will partiion the data into one year by one year squares. These are known as Lexis squares. 
        Similarly, we can imagine drawing diagonal lines at regular intervals, to represent the start of each calendar year. Drwaing these diagonal 
        lines starting at the start of each calendar year will partition the one year by one year Lexis squares into two triangles, an upper left triangle and a lower right triangle. 
        These triangles are known, unsurprisingly, as Lexis triangles, with the first type known as the upper triangle and the second the lower triangle. 
        
        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("What does this have to do with Lexis surfaces?")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        Lexis surfaces can be thought of as resulting from the process of counting the numbers of specific types of events that occur in Lexis squares or Lexis triangles. 
        For example, a Lexis surface of population structure as simply the population count (i.e. number of lines appearing it) for each triangle or line. 
        Similarly, death counts as simply the sum of death events recorded within each triangle or square. 

        Mortality rates are slightly more complicated, but fundamentally depend on the two above quantities. 

        These counts of events that occur in specific temporal 'areas' (the areas of age and time defined by the two primary axes of the Lexis diagram) are what is repesented graphically as the third axis of the Lexis surface, either as colour (a heatmap), contour lines (like a topographic map) or as height (using a true 3D surface plot). 

        """
                        )
                    )
                ],
                className = "mb-3"
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Relevance to this app")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
        This app cuts corners in one specific way: it makes use of Lexis squares rather than Lexis triangles. This means that the data presented do not quite follow genuine cohorts as they age. Despite this, diagonal disruptions and patterns in Lexis surface consistent with 
        cohort effects will often be apparent. The simplication, using Lexis squares not triangles, is made largely for pragmatic reasons but should be considered a limitation. 
        Lexis squares are often more commonly available and reported than Lexis triangles, and Lexis squares are more closely analogous to 'pixels' on a computer display, and elements in a 2 dimensional array of values, than Lexis triangles.    
        
        """
                        )
                    )
                ],
                className = "mb-3"
            )

        ],
        style = {
            "max-width" : "80%", 
            "margin-left" : "5%"
            }
    )    






