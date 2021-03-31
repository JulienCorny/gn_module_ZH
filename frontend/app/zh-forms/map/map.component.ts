import { Component, OnInit, AfterViewInit, OnDestroy } from "@angular/core";
import { Subscription } from "rxjs";
import { filter, map } from "rxjs/operators";
import { leafletDrawOption } from "@geonature_common/map/leaflet-draw.options";
import { CommonService } from "@geonature_common/service/common.service";
import { ModuleConfig } from "../../module.config";
import { MapService } from '@geonature_common/map/map.service';




@Component({
  selector: "zh-form-map",
  templateUrl: "map.component.html",
})
export class ZhFormMapComponent implements OnInit, AfterViewInit, OnDestroy {
  public leafletDrawOptions: any;
  public firstFileLayerMessage = true;
  public zhConfig = ModuleConfig;
  private $_geojsonSub: Subscription;

  public coordinates = null;
  public geometry = null;
  public firstGeom = true;

  constructor(
    private _commonService: CommonService,
    private _mapService: MapService
  ) { }

  ngOnInit() {
    // overight the leaflet draw object to set options
    // examples: enable circle =>  leafletDrawOption.draw.circle = true;
    leafletDrawOption.draw.circle = false;
    leafletDrawOption.draw.rectangle = false;
    leafletDrawOption.draw.marker = false;
    leafletDrawOption.draw.polyline = true;
    leafletDrawOption.edit.remove = false;
    this.leafletDrawOptions = leafletDrawOption;
    // set the input for the marker component
    // set the coord only when load data and when its edition mode (id_releve)
    // after the marker component does it by itself whith the ouput
    // when modifie the coordinates innput, it create twice the marker


    // to get geometry from filelayer
    this._mapService.gettingGeojson$.subscribe(geojson => {

    })
  }

  ngAfterViewInit() {
    if (this._mapService.currentExtend) {
      this._mapService.map.setView(
        this._mapService.currentExtend.center,
        this._mapService.currentExtend.zoom
      )
    }
    let filelayerFeatures = this._mapService.fileLayerFeatureGroup.getLayers();
    // si il y a encore des filelayer -> on désactive le marker par defaut
    if (filelayerFeatures.length > 0) {
      this._mapService.setEditingMarker(false);
      this._mapService.fileLayerEditionMode = true;
    }

    filelayerFeatures.forEach(el => {
      if ((el as any).getLayers()[0].options.color == "red") {
        (el as any).setStyle({ color: "green", opacity: 0.2 });
      }
    });
  }

  // display help toaster for filelayer
  infoMessageFileLayer() {
    if (this.firstFileLayerMessage) {
      this._commonService.translateToaster("info", "Map.FileLayerInfoMessage");
    }
    this.firstFileLayerMessage = false;
  }

  sendGeoInfo(geojson) {

  }

  ngOnDestroy() {

  }
}
