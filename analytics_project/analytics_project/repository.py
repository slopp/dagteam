from dagster import load_assets_from_package_module, repository

from analytics_project import assets


@repository
def analytics_project():
    return [load_assets_from_package_module(assets)]
