{
    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs/nixos-26.05";
    };

    outputs = { self, nixpkgs }: 
    let
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};
        libs = with pkgs; [
            stdenv.cc.cc.lib
            zlib
            zstd
            libglvnd
            libGL
            libGLU
            libxkbcommon
            wayland
            libxcb
            libx11
            libxcursor
            libxext
            libxfixes
            libxi
            libxrandr
            libxrender
            libxcb
            fontconfig
            freetype
            dbus
            glib
        ];
    in {
        # development environment
        devShells.${system}.default = pkgs.mkShell {
            buildInputs = libs;

            packages = [
                pkgs.python314
                pkgs.python314Packages.uv
                pkgs.python314Packages.ruff
                pkgs.basedpyright
            ];
        };

        packages.${system}.default = pkgs.writeShellApplication {
            name = "logging-off";

            runtimeInputs = libs;

            text = ''
                export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath libs}''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
                .venv/bin/pyuic6 -o src/view/ui/mainwindow.py src/view/ui/mainwindow.ui
                exec uv run src/main.py
            '';
        };
    };
}
