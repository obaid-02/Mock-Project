import dash
import json
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load Plotly figures (assuming you have JSON files for the figures)
with open('plots/unemployment_plot.json') as f:
    unemploymetnt_plot = json.load(f)

with open('plots/shareprice_plot.json') as f2:
    shareprice_plot = json.load(f2)

with open('plots/covidcases_plot.json') as f3:
    covidcases_plot = json.load(f3)

with open('plots/gdp_growth_entire_world-_by country.json') as f3:
    gdp_plot = json.load(f3)

with open('plots/inflation_entire_world-_by country.json') as f3:
    inflation_plot = json.load(f3)

with open('plots/Stringency_index_world_average.json') as f3:
    stringency_plot = json.load(f3)

with open('plots/Stringency_index_selected_countries.json') as f3:
    top_stringency_plot = json.load(f3)

with open('plots/gdp_growth_top_economies.json') as f3:
    top_gdp_plot = json.load(f3)

with open('plots/inflation_top_economies.json') as f3:
    top_inflation_plot = json.load(f3)

with open('plots/gdp_growth_four_countries.json') as f3:
    four_gdp_plot = json.load(f3)

with open('plots/inflation_four_countries.json') as f3:
    four_inflation_plot = json.load(f3)

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# App layout with navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    html.Nav([
        dcc.Link('Home', href='/'),
        html.Br(),
        dcc.Link('World Economy', href='/world-economics'),
        html.Br(),
        dcc.Link('Top Economies', href='/top-economies'),
    ], style={'padding': '10px'}),
    
    html.Div(id='page-content')
])

# Home Page Layout
home_layout = html.Div([
    html.Div(
    [
        html.Video(
            src='/assets/covidvideo.mp4',  # Ensure your video file is located in the 'assets' folder
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "object-fit": "cover",  # Ensures the video covers the entire div
                "z-index": "-1",  # Makes sure the video stays in the background
            },
        ),
        html.Div(
            [
                html.H1(
    "Effect of Covid on Global Economy",
    style={
        'font-family': 'Montserrat',
        'text-align': 'center',
        'color': 'white',
        'z-index': '1'
    }
),

                html.P(
                    '''This dashboard provides an in-depth analysis of COVID-19's 
                    impact on the global economy, covering key metrics like unemployment, 
                    share prices, GDP growth, and sector-specific disruptions''',
                    style={'text-align': 'center', 'color': 'white', 'z-index': '1'},
                    id='para_home'
                ),
            ],
            style={
                'padding': '20px',
                'position': 'relative',  # Ensures this content is above the video
                'z-index': '1',  # Ensures the content is above the video
                'border-radius': '10px',  # Optional: adds rounded corners
                'margin-top':'5px'
            }
        ),
    ],
    style={
        'position': 'relative',
        'height': '30vh',
        'width': '100%',
    }
),

    html.Div([
        html.P('''The COVID-19 pandemic has been a defining moment in modern 
               history, reshaping societies, healthcare systems, and most notably, the global 
               economy. From supply chain disruptions to mass unemployment, countries worldwide 
               faced unprecedented challenges. Many industries were forced to shut down, and 
               millions of workers transitioned to remote work or faced layoffs. While governments 
               implemented various fiscal measures, the impact of the pandemic continues to be felt 
               across different sectors, leaving profound scars on both developed and developing 
               economies.This dashboard provides a comprehensive analysis of the pandemic’s economic 
               effects, looking at GDP contractions, unemployment surges, and sector-specific 
               downturns. Data-driven insights will help illustrate the full scope of the pandemic's 
               influence, laying out the ripple effects that have disrupted global growth and 
               widened economic inequalities.''', id ="Pintro"),
        html.Video(src="/assets/economyfall.mp4",  autoPlay=True,
            loop=True,
            muted=True,
            style={'width': '100%', 'height': '100%'})
    ],  style={
        'display': 'flex',  
        'justify-content': 'space-between',  
        'align-items': 'center',  
        'gap': '100px', 
        'width': '90%',
        'height': '300px', 
        'margin-top': '20px',
        'margin-right': '20px',
        # 'border': '1px solid #ccc',  # Optional styling
        'padding': '10px'}),

    html.Div([
        html.H2("Plot for Daily Covid Cases Globally", style={'text-align': 'center', 'margin-top':'20px'}),
        dcc.Graph(id='shareprice', figure=covidcases_plot,style={'margin-bottom':'2px'}),
        html.A('''Database Source''', 
                       href='https://ourworldindata.org/covid-cases', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
    ], style={'padding-left': '40px'})    ,

    html.Footer([
    html.Div('Created by: Sheikh Obaid Ullah, Sri Karthik Siddharth and Titouan', style={'color': 'white'}),
   ], style={'background-color': '#333', 'color': 'white', 'padding': '10px','text-align':'center'})



])



# Page 1 Layout - World Economy
world_economy_layout = html.Div([
    html.Div(
    [
        html.Video(
            src='/assets/worldvideo.mp4',  # Ensure your video file is located in the 'assets' folder
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "object-fit": "cover",  # Ensures the video covers the entire div
                "z-index": "-1",  # Makes sure the video stays in the background
            },
        ),
        html.Div(
            [
                html.H1(
                    "Effect of Covid on World Economy",
                    style={'margin-left':'20px', 'color': 'black', 'z-index': '1'}  # White text for better readability
                ),
               html.P(
                [
                    "Visualizing global GDP growth, inflation, unemployment, and share price trends", 
                    html.Br(), 
                    "during and after COVID-19."
                ],
                style={'margin-left': '20px', 'color': 'black', 'z-index': '1'},
                id='para_home'
            ),
            ],
            style={
                'padding': '20px',
                'position': 'relative',  # Ensures this content is above the video
                'z-index': '1',  # Ensures the content is above the video
                'border-radius': '10px',  # Optional: adds rounded corners
                'margin-top':'5px'
            }
        ),
    ],
    style={
        'position': 'relative',
        'height': '30vh',
        'width': '100%',
    }
),
    html.Div([  
        html.H2("GDP Growth", style={'text-align': 'left'}),
        html.P("This graph illustrates the impact of the COVID-19 pandemic on the GDP growth of numerous countries from 2017 to 2023. The sharp decline in GDP growth observed in 2020 highlights the severe economic consequences of the pandemic. Subsequent years saw varying recovery rates across different countries, indicating diverse responses to the crisis and varying economic resilience.", style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=gdp_plot),
        html.A('''Database Source''', 
                       href='https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?end=2023&start=1961&view=chart', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Inflation Data", style={'text-align': 'left'}),
        html.P("This graph illustrates the inflation trends across various countries during and after the COVID-19 pandemic. The graph highlights a significant spike in inflation rates for many countries in 2021 and 2022, likely influenced by factors such as supply chain disruptions, increased demand, and government stimulus measures implemented in response to the pandemic. However, the graph also shows a notable decline in inflation rates in 2023, suggesting that some of the inflationary pressures may be easing.", style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=inflation_plot),
        html.A('''Database Source''', 
                       href='https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2023&start=1960&view=chart', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
           
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Stringency Index", style={'text-align': 'left'}),
        html.P('''The period of time covered by the database for the "stringency_index" value 
               varies from one country to another. We observe a first increase of the 
               "stringency_index" in January (e.g. in China), a global peak in March, 
               then a slow decrease, especially after June.''', style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=stringency_plot),
         html.A('''Database Source: Vitenu-Sackey, Prince Asare (2020), 
                       “The Impact of Covid-19 Pandemic on the Global Economy: Emphasis on 
                       Poverty Alleviation and Economic Growth”, Mendeley Data, V1, 
                       doi: 10.17632/b2wvnbnpj9.1''', 
                       href='https://data.mendeley.com/datasets/b2wvnbnpj9/1', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Unemployment Data", style={'text-align': 'left'}),
        html.P("The COVID-19 pandemic caused a significant spike in global unemployment, with the number of unemployed persons reaching its highest point in 2020. The graph shows a sharp increase in unemployment beginning in 2019, followed by a period of fluctuation with some recovery but still remaining above pre-pandemic levels.", style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=unemploymetnt_plot),
         html.A('''Database Source''', 
                       href='https://www.statista.com/', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([
        html.H2("Share Price Trends", style={'text-align': 'left'}),
        html.P('''This plot shows the share price index trends for major developed and 
               emerging economies from January 2019 to June 2023. It highlights the 
               effects of the COVID-19 pandemic, with a significant dip in early 2020 
               followed by varied recovery rates across different countries.''', 
               style={'text-align': 'left'}),
        dcc.Graph(id='shareprice', figure=shareprice_plot),
        html.A('''Database Source''', 
                       href='https://www.statista.com/', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0'})
])

# Page 2 Layout - Top Economies (Placeholder for now)
top_economies_layout = html.Div([
    html.Div(
    [
        html.Video(
            src='/assets/topeconomy.mp4',  # Ensure your video file is located in the 'assets' folder
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "object-fit": "cover",  # Ensures the video covers the entire div
                "z-index": "-1",  # Makes sure the video stays in the background
            },
        ),
        html.Div(
            [
                html.H1(
                    "Effect of Covid on Top Economies",
                    style={'margin-left':'20px', 'color': 'black', 'z-index': '1'}  # White text for better readability
                ),
                html.P(
                    '''Exploring COVID-19's effects on GDP, inflation, and unemployment in major global economies.''',
                    style={'margin-left':'20px', 'color': 'black', 'z-index': '1'},
                    id='para_home'
                ),
            ],
            style={
                'padding': '20px',
                'position': 'relative',  # Ensures this content is above the video
                'z-index': '1',  # Ensures the content is above the video
                'border-radius': '10px',  # Optional: adds rounded corners
                'margin-top':'5px'
            }
        ),
    ],
    style={
        'position': 'relative',
        'height': '30vh',
        'width': '100%',
    }
),
    html.H3('''For the top-economies such as the United States, China, Japan, Germany, 
            and India—GDP and inflation trends from 2015 to 2024 showed distinct but 
            interrelated patterns:'''),
    html.Div([  
        html.H2("GDP Growth", style={'text-align': 'left'}),
        html.P(''' GDP: Before COVID-19, most of these economies experienced steady GDP growth. 
               The pandemic caused a sharp GDP contraction in 2020, especially in developed 
               economies like the U.S., Japan, and Germany. However, recovery began in 2021, 
               with emerging markets like India rebounding strongly. By 2024, most had surpassed 
               pre-pandemic GDP levels, though growth rates varied due to differences in fiscal 
               policy and sectoral resilience.''', style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=top_gdp_plot),
         html.A('''Database Source''', 
                       href='https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?end=2023&start=1961&view=chart', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
                
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Inlation rate", style={'text-align': 'left'}),
        html.P(''' Inflation: Inflation was largely stable until 2020. During the pandemic, 
               inflation initially declined, especially in consumer-driven economies like the U.S. 
               and Germany. But as economies reopened, inflation surged in 2021–2022, hitting the U.S. 
               particularly hard due to high demand and supply bottlenecks. Emerging economies faced 
               similar trends, although with variations depending on energy dependence and domestic 
               policies. By 2024, inflation began stabilizing in most top economies, though energy and 
               supply chain vulnerabilities kept some pressure on prices.''', style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=top_inflation_plot),
         html.A('''Database Source''', 
                       href='https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2023&start=1960&view=chart', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
           
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Stringency Index", style={'text-align': 'left'}),
        html.P('''Due to limited testing, the number of "confirmed cases" is 
               lower than the true number of infections. In particular, the first 
               Covid-19 waves in 2020 had less "confirmed cases" than the subsequent 
               years, but came with a lock-down in a number of countries. As a consequence, 
               the number of confirmed cases alone may not explain the changes in economy. 
               The "Stringency Index" seems to be a relevant metrics in the study of the 
               impact of Covid-19 on global economy. By definition, "the stringency index 
               is a composite measure based on nine response indicators including school 
               closures, workplace closures, and travel bans, rescaled to a value from 
               0 to 100 (100 = strictest).''', style={'text-align': 'left'}),
            dcc.Graph(id='unemployement', figure=top_stringency_plot),
            html.A('''Database Source: Vitenu-Sackey, Prince Asare (2020), 
                       “The Impact of Covid-19 Pandemic on the Global Economy: Emphasis on 
                       Poverty Alleviation and Economic Growth”, Mendeley Data, V1, 
                       doi: 10.17632/b2wvnbnpj9.1''', 
                       href='https://data.mendeley.com/datasets/b2wvnbnpj9/1', 
                       target='_blank', style={'color': 'blue', 'margin-top':'0px','font-size': '10px'})
                
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    
html.H2("Plots on some other Economies", 
        style={'text-align': 'center', 'animation': 'colorChange 3s infinite'}),
    html.Div([
        html.Div([  
        html.H2("GDP Growth", style={'text-align': 'left'}),
        html.P("The COVID-19 pandemic severely impacted the GDP growth of China, France, India, and Morocco. In 2020, all four countries experienced significant declines. While China recovered strongly in 2021, France, India, and Morocco had slower recoveries, highlighting the varying impact of the pandemic on different economies.", style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=four_gdp_plot)
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),

    html.Div([  
        html.H2("Inflation Rate", style={'text-align': 'left'}),
        html.P("The graph shows inflation rates for China, France, India, and Morocco from 2014 to 2023. All four countries experienced a significant peak in inflation rates around 2021-2022 due to the economic disruptions caused by the COVID-19 pandemic.", style={'text-align': 'left'}),
        dcc.Graph(id='unemployement', figure=four_inflation_plot)
    ], style={'padding': '20px', 'background-color': '#ffffff', 'border': '1px solid #e0e0e0', 'margin-bottom': '20px'}),
    ])
])

# Callback to render pages based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    # Display layout based on the URL path
    if pathname == '/world-economics':
        return world_economy_layout  # Show World Economy page when "/page-1"
    elif pathname == '/top-economies':
        return top_economies_layout  # Show Top Economies page when "/page-2"
    return home_layout  # Default to Home page

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
