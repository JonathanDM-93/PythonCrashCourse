import folium
from folium.plugins import MiniMap

# Datos de las aduanas (asegúrate de añadir todas las aduanas restantes)
aduanas_internas = [
    {"nombre": "Aduana de Aguascalientes", "latitud": 21.8833, "longitud": -102.2916},
    {"nombre": "Aduana del AICM", "latitud": 19.4361, "longitud": -99.0719},
    {"nombre": "Aduana de Celaya", "latitud": 20.5235, "longitud": -100.8150},
    {"nombre": "Aduana de Guadalajara", "latitud": 20.6597, "longitud": -103.3496},
    {"nombre": "Aduana de Guanajuato", "latitud": 21.0190, "longitud": -101.2574},
    {"nombre": "Aduana de México (Pantaco)", "latitud": 19.4511, "longitud": -99.1255},
    {"nombre": "Aduana de Puebla", "latitud": 19.0414, "longitud": -98.2063},
    {"nombre": "Aduana de Querétaro", "latitud": 20.5888, "longitud": -100.3899},
    {"nombre": "Aduana de San Luis Potosí", "latitud": 22.1565, "longitud": -100.9855},
    {"nombre": "Aduana de Toluca", "latitud": 19.2826, "longitud": -99.6557},
    {"nombre": "Aduana de Torreón", "latitud": 25.5439, "longitud": -103.4190},
    {"nombre": "Aduana de Ciudad Hidalgo (Michoacán)", "latitud": 19.6823, "longitud": -100.5528}
]

aduanas_frontera_norte = [
    {"nombre": "Aduana de Agua Prieta", "latitud": 31.3322, "longitud": -109.5484},
    {"nombre": "Aduana de Ciudad Acuña", "latitud": 29.3232, "longitud": -100.9570},
    {"nombre": "Aduana de Ciudad Camargo", "latitud": 26.3044, "longitud": -98.7120},
    {"nombre": "Aduana de Ciudad Juárez", "latitud": 31.7383, "longitud": -106.4875},
    {"nombre": "Aduana de Matamoros", "latitud": 25.8693, "longitud": -97.5027},
    {"nombre": "Aduana de Mexicali", "latitud": 32.6633, "longitud": -115.4678},
    {"nombre": "Aduana de Nogales", "latitud": 31.3323, "longitud": -110.9343},
    {"nombre": "Aduana de Nuevo Laredo", "latitud": 27.5036, "longitud": -99.5075},
    {"nombre": "Aduana de Ojinaga", "latitud": 29.5678, "longitud": -104.4167},
    {"nombre": "Aduana de Piedras Negras", "latitud": 28.7041, "longitud": -100.5235},
    {"nombre": "Aduana de Reynosa", "latitud": 26.0922, "longitud": -98.2776},
    {"nombre": "Aduana de Tecate", "latitud": 32.5714, "longitud": -116.6264},
    {"nombre": "Aduana de Tijuana", "latitud": 32.5335, "longitud": -117.0182}
]

aduanas_frontera_sur = [
    {"nombre": "Aduana de Ciudad Hidalgo (Chiapas)", "latitud": 14.6925, "longitud": -92.3934},
    {"nombre": "Aduana de Subteniente López (Chetumal)", "latitud": 18.5004, "longitud": -88.2966},
    {"nombre": "Aduana de Suchiate", "latitud": 14.5341, "longitud": -92.1462},
    {"nombre": "Aduana de Tenosique", "latitud": 17.4750, "longitud": -91.4297}
]

aduanas_maritimas = [
    {"nombre": "Aduana de Acapulco", "latitud": 16.8635, "longitud": -99.8901},
    {"nombre": "Aduana de Altamira", "latitud": 22.4038, "longitud": -97.9391},
    {"nombre": "Aduana de Cancún", "latitud": 21.1619, "longitud": -86.8515},
    {"nombre": "Aduana de Ciudad del Carmen", "latitud": 18.6483, "longitud": -91.8313},
    {"nombre": "Aduana de Coatzacoalcos", "latitud": 18.1527, "longitud": -94.4236},
    {"nombre": "Aduana de Ensenada", "latitud": 31.8667, "longitud": -116.5964},
    {"nombre": "Aduana de Guaymas", "latitud": 27.9256, "longitud": -110.8975},
    {"nombre": "Aduana de Lázaro Cárdenas", "latitud": 17.9585, "longitud": -102.1943},
    {"nombre": "Aduana de Manzanillo", "latitud": 19.0500, "longitud": -104.3167},
    {"nombre": "Aduana de Mazatlán", "latitud": 23.2494, "longitud": -106.4110},
    {"nombre": "Aduana de Progreso", "latitud": 21.2833, "longitud": -89.6667},
    {"nombre": "Aduana de Puerto Morelos", "latitud": 20.8540, "longitud": -86.8770},
    {"nombre": "Aduana de Tampico", "latitud": 22.2553, "longitud": -97.8689},
    {"nombre": "Aduana de Topolobampo", "latitud": 25.6000, "longitud": -109.0500},
    {"nombre": "Aduana de Tuxpan", "latitud": 20.9579, "longitud": -97.4087},
    {"nombre": "Aduana de Veracruz", "latitud": 19.1817, "longitud": -96.1429}
]

# Centro del mapa en México
ubicacion_mexico = [23.6345, -102.5528]

# Crear el mapa
mapa_mexico = folium.Map(location=ubicacion_mexico, tiles="OpenStreetMap", zoom_start=5)


# Función para añadir marcadores con diferentes iconos y tooltips
def agregar_marcadores(aduanas, icono, color):
    for aduana in aduanas:
        folium.Marker(
            location=[aduana["latitud"], aduana["longitud"]],
            popup=folium.Popup(aduana["nombre"], parse_html=True, sticky=True),
            tooltip=aduana["nombre"],
            icon=folium.Icon(icon=icono, color=color)
        ).add_to(mapa_mexico)


# Añadir marcadores para cada grupo de aduanas con diferentes iconos
agregar_marcadores(aduanas_internas, 'glyphicon glyphicon-map-marker', 'blue')
#agregar_marcadores(aduanas_frontera_norte, 'flag', 'green')
#agregar_marcadores(aduanas_frontera_sur, 'flag', 'red')
#agregar_marcadores(aduanas_maritimas, 'flag', 'purple')

# Añadir leyenda al mapa
legend_html = '''
     <div style="position: fixed; 
     bottom: 200px; left: 200px; width: 200px; height: 140px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white;">
     &nbsp;<b>Aduanas de México:</b><br>
     &nbsp;<i class="fa-solid fa-map-pin" style="color:#4682B4"></i>&nbsp;Internas<br>
     &nbsp;<i class="fa-solid fa-map-pin" style="color:#008000"></i>&nbsp;Frontera Norte<br>
     &nbsp;<i class="fa-solid fa-map-pin" style="color:red"></i>&nbsp;Frontera Sur<br>
     &nbsp;<i class="fa-solid fa-map-pin" style="color:#DA70D6"></i>&nbsp;Marítimas<br>
     </div>
     '''

mapa_mexico.get_root().html.add_child(folium.Element(legend_html))

# Guardar el mapa como HTML
mapa_html = 'mapa_aduanas_mexico.html'

# Crear el minimapa
minimapa = MiniMap()

# Agregar el minimapa al mapa principal
mapa_mexico.add_child(minimapa)

# Guardar el mapa
mapa_mexico.save(f"C:/Users/joni_/OneDrive/Escritorio/{mapa_html}")

print(f"Mapa guardado como {mapa_html}")
