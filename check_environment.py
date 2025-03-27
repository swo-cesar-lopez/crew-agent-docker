#!/usr/bin/env python

"""
Este script verifica que el entorno Docker tenga todas las dependencias necesarias
y muestra información básica del sistema.
"""

import sys
import subprocess
import pkg_resources

def check_package(package_name):
    try:
        dist = pkg_resources.get_distribution(package_name)
        print(f"✅ {package_name}: {dist.version}")
        return True
    except pkg_resources.DistributionNotFound:
        print(f"❌ {package_name}: No instalado")
        return False

def main():
    print(f"Python versión: {sys.version}")
    print("\nVerificando paquetes esenciales:")
    
    # Lista de paquetes esenciales a verificar
    packages = [
        "crewai", 
        "crewai_tools", 
        "langchain_community",
        "langchain-groq", 
        "fastapi", 
        "uvicorn", 
        "pydantic", 
        "setuptools",
        "uvloop",
        "httptools"
    ]
    
    all_installed = True
    for package in packages:
        if not check_package(package):
            all_installed = False
    
    print("\nEstado del sistema:")
    print(f"{'✅' if all_installed else '❌'} Todos los paquetes esenciales están instalados")
    
    # Verificar variables de entorno
    print("\nVariables de entorno requeridas:")
    env_vars = ["SERPER_API_KEY", "GROQ_API_KEY", "OPENAI_API_KEY"]
    for var in env_vars:
        import os
        if os.getenv(var):
            masked_value = os.getenv(var)[:4] + "..." + os.getenv(var)[-4:] if len(os.getenv(var)) > 8 else "***"
            print(f"✅ {var}: {masked_value}")
        else:
            print(f"❌ {var}: No configurado")

if __name__ == "__main__":
    main()
