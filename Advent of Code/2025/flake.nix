{
  description = "Advent of Code 2025";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    with nixpkgs.lib;
    with flake-utils.lib;

    eachSystem allSystems (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {
        devShells.default =
          with pkgs;
          mkShell {
            buildInputs = with haskellPackages; [
              (ghcWithPackages (hp: [
                hp.regex-pcre
                hp.split
              ]))
              haskell-language-server
              ormolu
            ];
          };
      }
    );
}
