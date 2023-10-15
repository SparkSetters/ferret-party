"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.NFTController = void 0;
const common_1 = require("@nestjs/common");
const child_process_1 = require("child_process");
let NFTController = class NFTController {
    runNFTTool(data) {
        return __awaiter(this, void 0, void 0, function* () {
            return new Promise((resolve, reject) => {
                var _a, _b;
                const pythonProcess = (0, child_process_1.exec)(`python ./services/nft_tool.py ${data.topic} ${data.industry1} ${data.industry2} ${data.exclusion1} ${data.exclusion2} ${data.date_start} ${data.date_end}`);
                let result = '';
                (_a = pythonProcess.stdout) === null || _a === void 0 ? void 0 : _a.on('data', (data) => {
                    result += data.toString();
                });
                (_b = pythonProcess.stderr) === null || _b === void 0 ? void 0 : _b.on('data', (data) => {
                    console.error(`stderr: ${data}`);
                });
                pythonProcess.on('close', (code) => {
                    if (code !== 0) {
                        return reject(new Error(`Python script exited with code ${code}`));
                    }
                    return resolve(result);
                });
            });
        });
    }
};
exports.NFTController = NFTController;
__decorate([
    (0, common_1.Post)('run'),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], NFTController.prototype, "runNFTTool", null);
exports.NFTController = NFTController = __decorate([
    (0, common_1.Controller)('nft')
], NFTController);
