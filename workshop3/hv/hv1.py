import numpy as np
import holoviews as hv
hv.extension('bokeh')

# Source: https://holoviews.org/user_guide/Deploying_Bokeh_Apps.html

# Declare some points
points = hv.Points(np.random.randn(1000,2 ))

# Declare points as source of selection stream
selection = hv.streams.Selection1D(source=points)

# Write function that uses the selection indices to slice points and compute stats
def selected_info(index):
    arr = points.array()[index]
    if index:
        label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
    else:
        label = 'No selection'
    return points.clone(arr, label=label).opts(color='red')

# Combine points and DynamicMap
selected_points = hv.DynamicMap(selected_info, streams=[selection])
layout = points.opts(tools=['box_select', 'lasso_select']) + selected_points

#layout

hv.save(layout, 'out.html')

