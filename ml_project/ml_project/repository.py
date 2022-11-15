from dagster import load_assets_from_package_module, repository, RunRequest, define_asset_job, SourceAsset
from dagster import AssetKey, EventLogEntry, SensorEvaluationContext, asset_sensor

from ml_project import assets

# define a sensor that updates the penguin cluster asset
# when the upstream asset updates
penguins = SourceAsset(key = AssetKey("penguins"))

update_penguin_cluster = define_asset_job("update_penguin_cluster", selection = "penguin_cluster")

@asset_sensor(asset_key=AssetKey("penguins"), job=update_penguin_cluster)
def update_penguin_cluster_sensor(context: SensorEvaluationContext, asset_event: EventLogEntry):
    yield RunRequest(run_key=context.cursor)



@repository
def ml_project():
    return [load_assets_from_package_module(assets), [update_penguin_cluster_sensor]]
