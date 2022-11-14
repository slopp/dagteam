from dagster import load_assets_from_package_module, repository

from ml_project import assets


@repository
def ml_project():
    return [load_assets_from_package_module(assets)]
