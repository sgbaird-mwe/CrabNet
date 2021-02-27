from distutils.core import setup
setup(
  name = 'ElM2D',        
  packages = ['ElM2D'],  
  version = '0.1.0',      
  license='GPL3',       
  description = 'A mapping class to perform the ElMD metric on datasets on ionic compositions',  
  author = 'Cameron Hagreaves',              
  author_email = 'cameron.h@rgreaves.me.uk', 
  url = 'https://github.com/lrcfmd/ElM2D/',   
  download_url = 'https://github.com/lrcfmd/ElM2D/archive/v0.1.0.tar.gz',    
  keywords = ['ChemInformatics', 'Materials Science', 'Machine Learning', 'Materials Representation'],   
  install_requires=[            
          'numpy',
          'pandas',
          'scipy',
          'plotly',
          'umap-learn',
          'numba'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',  
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3) ',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)