// Solitons.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "material.h"
#include "primitives/slab/isoslab/slab.h"
#include "primitives/section/section.h"
#include "meshgrid.hpp"

int main()
{
    //wavelength
    global.lambda = 1.064;
    global.N = 20;
    global.polarisation = TE;
    
    Material sio(1.45);
    Material helium(1.02451);
    Material air(1.0);
    
    //UniformSlab core(1.5e-6, sio);
    //UniformSlab top(15e-9, helium);
    //UniformSlab air(1e-6, air);

    Slab main_core(air(1) + helium(15e-9*1e6) + sio(1.5) + air(1));

    main_core.find_modes();



    auto x = meshgen::linspace(0.0, 1.0, 100);
    auto y = meshgen::linspace(0.0, 1.0, 100);
    auto z = meshgen::linspace(0.0, 1.0, 100);

    meshgen::mesh_grid<double, 0, 2> X;
    meshgen::mesh_grid<double, 1, 2> Y;
    meshgen::mesh_grid<double, 2, 2> Z;

    std::tie(X, Y) = meshgen::meshgrid(x, y);


    for (size_t i = 0; i < X.size1(); ++i) {
        for (size_t j = 0; j < X.size2(); ++j) {
           Z(i, j)   main_core.get_mode(1)->field(Coord(X(i, j), Y(i, j))).E1;
        }
    }


    std::cout << "Fundamental mode has kz = " << main_core.get_mode(1)->get_kz() << std::endl;
    std::cout << "Fundamental mode has neff = " << main_core.get_mode(1)->n_eff() << std::endl;
    std::cout << "Hello World!\n";
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
