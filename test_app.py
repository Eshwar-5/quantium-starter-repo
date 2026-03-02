from dash.testing.application_runners import import_app


def test_001_header_present(dash_duo):
    # Looks for the app object in app.py
    app = import_app("app")
    dash_duo.start_server(app)

    # Assertions
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").is_displayed()


def test_002_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#visualisation", timeout=10)
    assert dash_duo.find_element("#visualisation").is_displayed()


def test_003_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#region-picker", timeout=10)
    assert dash_duo.find_element("#region-picker").is_displayed()