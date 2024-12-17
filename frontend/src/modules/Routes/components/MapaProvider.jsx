import { Mapa } from "../../principalPages/generalMap/components/Mapa";
import { FilterProvider } from "../../principalPages/generalMap/context/FilterContext";
import { GeolocationProvider } from "../../principalPages/generalMap/context/GeolocationsContext";
import { InfoProvider } from "../../principalPages/generalMap/context/InfoContext";

export function MapaProvider() {
    return (
        <FilterProvider>
            <GeolocationProvider>
                <InfoProvider>
                    <Mapa/>
                </InfoProvider>
            </GeolocationProvider>
        </FilterProvider>
    )
}