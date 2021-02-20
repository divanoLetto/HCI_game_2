from settings import GRIDWIDTH, GRIDHEIGHT, TILESIZE

num_actions = 6  # 4
max_episode_timesteps = 100
with_property_embedding = True

scale_global_view = [int(GRIDWIDTH / TILESIZE), int(GRIDHEIGHT / TILESIZE)]
num_local_views = 2
scales_local_views = [3, 5]
num_channels_map = 1
nums_values_channel = [8]  # massimo valore che posso trovare nelle mappe

num_property_views = 2
scales_property_views = [4, 4]  # due array di quattro elementi
nums_values_property = [19, 19]  # massimi valori presenti nelle proprietà

ON_TRAINING_PRINT_MAP_DURING_STEPS = False
ON_TRAINING_PRINT_INFO_DURING_STEPS = False
