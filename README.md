See the `conf.py`:
```
scheme = 'B'

schemeA = {
    'image_name': 'd1.jpg',
    'is_lama': False,
    'inpaint_radius': 3,
    'is_gaussianblur': True,
    'gaussian_radius': 9 # Odd number
}

schemeB = {
    'image_name': 'd1.jpg',
    'gaussian_radius': 51, # Odd number
    'is_use_fill_color': False,
    'fill_color': [227, 234, 244]
}
```
You can choose scheme whcih you want.<br>
The A is useof openCV inpaint or model(LaMa); And B is useof openCV but no inpaint.<br>
When you finished the conf, run `python main.py`.<br>
<br>
If you have a better scheme, please connect me.<br>
Email: xiadongliang88@163.com<br>