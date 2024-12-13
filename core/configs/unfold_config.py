from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD_THEME_SWITCH = True

UNFOLD = {
    "DASHBOARD_CALLBACK": "apps.common.views.dashboard_callback",
    "SITE_TITLE": "ECommerceDemo Admin Panel",
    "SITE_HEADER": "ECommerceDemo",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("imgs/logo.png"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("imgs/logo.png"),  # light mode
        "dark": lambda request: static("imgs/logo_dark.png"),  # dark mode
    },
    # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    "SITE_LOGO": {
        "light": lambda request: static("imgs/logo.png"),  # light mode
        "dark": lambda request: static("imgs/logo_dark.png"),  # dark mode
    },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("imgs/logo.png"),
        },
    ],
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    # "THEME": "dark",  # Force theme: "dark" or "light". Will disable theme switcher
    # "LOGIN": {
    #     "image": lambda request: static("sample/login-bg.jpg"),
    #     "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
    # },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    # "COLORS": {
    #     "font": {
    #         "subtle-light": "107 114 128",
    #         "subtle-dark": "156 163 175",
    #         "default-light": "75 85 99",
    #         "default-dark": "209 213 219",
    #         "important-light": "17 24 39",
    #         "important-dark": "243 244 246",
    #     },
    #     "primary": {
    #         "50": "250 245 255",
    #         "100": "243 232 255",
    #         "200": "233 213 255",
    #         "300": "216 180 254",
    #         "400": "192 132 252",
    #         "500": "168 85 247",
    #         "600": "147 51 234",
    #         "700": "126 34 206",
    #         "800": "107 33 168",
    #         "900": "88 28 135",
    #         "950": "59 7 100",
    #     },
    # },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [

            {
                "title": _(""),
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        # "badge": "sample_app.badge_callback",
                        "permission": lambda request: request.user.is_superuser,
                    },
                    # {
                    #     "title": _("Users"),
                    #     "icon": "people",
                    #     "link": reverse_lazy("admin:index"),
                    # },
                ],
            },
            {
                "title": _("Products"),
                "icon": "shopping_cart",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:products_category_changelist"),
                    },
                    {
                        "title": _("Products"),
                        "icon": "store",
                        "link": reverse_lazy("admin:products_product_changelist"),
                    },
                    {
                        "title": _("Size Groups"),
                        "icon": "straighten",
                        "link": reverse_lazy("admin:products_sizegroup_changelist"),
                    },
                    {
                        "title": _("Colors"),
                        "icon": "palette",
                        "link": reverse_lazy("admin:products_color_changelist"),
                    },
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             # "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:index"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}
