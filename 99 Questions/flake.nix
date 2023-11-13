{
  description = "";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    with nixpkgs.lib;
    with flake-utils.lib;

    eachSystem allSystems (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {
        devShells.default = with pkgs; mkShell {
          buildInputs = with haskellPackages; [
            ghc
            haskell-language-server
          ];
        };
      });
}
