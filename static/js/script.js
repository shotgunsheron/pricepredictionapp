const stars = [].slice.call(document.querySelectorAll('.star'));

stars.forEach(elem => {
    elem.addEventListener('click', e => {
        const current = parseInt(e.target.dataset.value);

        const maxSelected = Math.max(
            ...stars.filter(elem => elem.style.color === 'yellow').map(x => x.dataset.value)
        );
        
        if(maxSelected === current){
            stars.forEach(elem => elem.style.color = 'black');
            document.getElementById('product_rating').value = '0';
        }else{

            stars
            .filter(elem => parseInt(elem.dataset.value) >= current)
            .forEach(elem => elem.style.color = 'black');

            stars
            .filter(elem => parseInt(elem.dataset.value) <= current)
            .forEach(elem => elem.style.color = 'yellow');
            
            document.getElementById('product_rating').value = `${current}`;
        }
    });
})

// -------------------------------------------------------------------------------------

/*
const options = ['USBCables', 'WirelessUSBAdapters', 'HDMICables', 'SmartTelevisions', 'RemoteControls', 'StandardTelevisions', 'TVWall&CeilingMounts', 'RCACables', 'Mounts', 'OpticalCables', 'Projectors', 'Adapters', 'SatelliteReceivers', 'DVICables', 'SpeakerCables', 'StreamingClients', 'AVReceivers&Amplifiers', 'TowerSpeakers', '3DGlasses', 'SmartWatches', 'PowerBanks', 'Smartphones', 'MicroSD', 'BasicMobiles', 'In-Ear', 'AutomobileChargers', 'Cradles', 'WallChargers', 'OTGAdapters', 'Tripods', 'SelfieSticks', 'Stands', 'CableConnectionProtectors', 'DÃ©cor', 'ScreenProtectors', 'StylusPens', 'Bedstand&DeskMounts', 'BasicCases', 'HandlebarMounts', 'On-Ear', 'CameraPrivacyCovers', 'PhoneCharms', 'Shower&WallMounts', 'PenDrives', 'Mice', 'GraphicTablets', 'Lapdesks', 'NotebookComputerStands', 'Keyboards', 'Condenser', 'DisposableBatteries', 'GelInkRollerballPens', 'Tape', 'Keyboard&MouseSets', 'ExternalHardDisks', 'VideoCameras', 'Tabletop&TravelTripods', 'Scientific', 'Repeaters&Extenders', 'TripodLegs', 'InkjetInkCartridges', 'DustCovers', 'GamingMice', 'Paints', 'MousePads', 'HardDiskBags', 'Macro&RinglightFlashes', 'NetworkingDevices', 'Routers', 'Over-Ear', 'BluetoothSpeakers', 'GeneralPurposeBatteries&BatteryChargers', 'WireboundNotebooks', 'RechargeableBatteries', 'BluetoothAdapters', 'USBtoUSBAdapters', 'CompleteTripodUnits', 'Notepads&MemoBooks', 'Film', 'Monitors', 'Lamps', 'CleaningKits', 'DomeCameras', 'Gamepads', 'Basic', 'USBHubs', 'PCMicrophones', 'OutdoorSpeakers', 'LaptopSleeves&Slipcases', 'ExternalMemoryCardReaders', 'BottledInk', 'CompositionNotebooks', 'RetractableBallpointPens', 'EthernetCables', 'Memory', 'UninterruptedPowerSupplies', 'Cases', 'SecureDigitalCards', 'SelfieLights', 'Webcams', 'CoolingPads', 'LaptopAccessories', 'Adapters&Multi-Outlets', 'ColouredPaper', 'InternalSolidStateDrives', 'MultimediaSpeakerSystems', 'DataCards&Dongles', 'LaptopChargers&PowerSupplies', 'PCSpeakers', 'BatteryChargers', 'StickBallpointPens', 'WoodenPencils', 'InternalHardDrives', 'Printers', 'Pens', 'SATACables', 'PCHeadsets', 'GamingKeyboards', 'SoundbarSpeakers', 'Earpads', 'InkjetPrinters', 'ColouringPens&Markers', 'Headsets', 'ExternalSolidStateDrives', 'PowerLANAdapters', 'InkjetInkRefills&Kits', 'Notebooks,WritingPads&Diaries', 'BackgroundSupports', 'Financial&Business', 'SurgeProtectors', 'Tablets', 'CordManagement', 'PaintingMaterials', 'TonerCartridges', 'LiquidInkRollerballPens', 'FountainPens', 'Caddies', 'TraditionalLaptops', 'ElectricKettles', 'ElectricHeaters', 'FanHeaters', 'LintShavers', 'DigitalKitchenScales', 'Choppers', 'InductionCooktop', 'HandBlenders', 'DryIrons', 'MixerGrinders', 'InstantWaterHeaters', 'RoomHeaters', 'Kettle&ToasterSets', 'StorageWaterHeaters', 'ImmersionRods', 'AirFryers', 'LaundryBaskets', 'SteamIrons', 'JuicerMixerGrinders', 'HandheldVacuums', 'EggBoilers', 'SandwichMakers', 'MiniFoodProcessors&Choppers', 'DigitalScales', 'VacuumSealers', 'CeilingFans', 'CanisterVacuums', 'PressureWashers,Steam&WindowCleaners', 'HalogenHeaters', 'Pop-upToasters', 'HeatConvectors', 'ElectricGrinders', 'ExhaustFans', 'DripCoffeeMachines', 'WaterPurifierAccessories', 'WaterCartridges', 'Rice&PastaCookers', 'AirPurifiers&Ionizers', 'Wet-DryVacuums', 'HEPAAirPurifiers', 'WaterFilters&Purifiers', 'LaundryBags', 'Sewing&EmbroideryMachines', 'SprayBottles', 'HandMixers', 'WetGrinders', 'OvenToasterGrills', 'Juicers', 'SmallKitchenAppliances', 'DigitalBathroomScales', 'EspressoMachines', 'TableFans', 'MilkFrothers', 'Humidifiers', 'StandMixerAccessories', 'RoboticVacuums', 'YogurtMakers', 'ColdPressJuicers', 'Split-SystemAirConditioners', 'SmallApplianceParts&Accessories', 'WaffleMakers&Irons', 'StovetopEspressoPots', 'MeasuringSpoons', 'CoffeePresses', 'RotiMakers', 'FanParts&Accessories', 'StandMixers', 'PedestalFans', 'HandheldBags'];
options.sort();

const selectElem = document.getElementById('product_category');

for(const option of options){
    const elem = document.createElement('option');
    elem.value = option;
    elem.innerText = option;

    selectElem.appendChild(elem);
}
*/


const submitButton = document.querySelector('.submit');

submitButton.addEventListener('click', e => {
    e.preventDefault();

    const category = document.getElementsByName('category')[0].value;
    const mPrice = document.getElementsByName('mPrice')[0].value;
    const rating = document.getElementsByName('rating')[0].value;

		const jsonData = {
			category, mPrice, rating
		}

    fetch('/submit',{
        method: "POST",
        body: JSON.stringify(jsonData)
    })
    .then(res => res.text())
    .then(res => {
        console.log(res);
				res = res.split(',')
        document.querySelector('.finalOutput').innerHTML = `Based on your input, our AI systems predicted that your product falls in the <u>${res[1]}</u> category and it predicted an optimal price of <u>$${res[0]}</u> for this product`;
        document.querySelector('.finalOutput').style.display = 'block';
    })
})