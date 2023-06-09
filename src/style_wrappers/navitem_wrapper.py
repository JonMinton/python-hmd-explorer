from dash import html
import dash_bootstrap_components as dbc


def makeNavItem(iconClassName, navLinkText, navLinkUrl):
    return dbc.NavItem(
        children = [
            html.I(className = iconClassName),
            dbc.NavLink(
                children = navLinkText,
                href = navLinkUrl,
                target = "_blank",
                style = {"color" : "rgba(50, 50, 50, 0.8)"}
            )
        ],
        className = "d-flex align-items-center",
        style = {"flex-direction" : "column"}
    )